from django.shortcuts import render, redirect
from django import forms
from .models import *

# Create your views here.
class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'


class JoinWaitlistForm(forms.ModelForm):
    class Meta:
        model = Waitlist
        fields = '__all__'

# views 
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
        
