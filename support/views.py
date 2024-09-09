from django.shortcuts import render, redirect
from .forms import MessageForm, JoinWaitlistForm

# Create your views here. 
def index(request):
    return render(request, 'index.html')

def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = MessageForm()

    return render(request, 'create_message.html', {'form': form})
        
def add_waitlist(request):
    if request.method == 'POST':
        form = JoinWaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    else:
        form = JoinWaitlistForm()

    return render(request, 'add_waitlist.html', {'form': form})
        
