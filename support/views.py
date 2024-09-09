from django.shortcuts import render, redirect
from .forms import MessageForm, JoinWaitlistForm
from django.contrib import messages

# Create your views here. 
def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST) if 'message_form_submit' in request.POST else MessageForm()
        waitlist = JoinWaitlistForm(request.POST) if 'waitlist_form_submit' in request.POST else JoinWaitlistForm()

        # Handle message form submission
        if 'message_form_submit' in request.POST and form.is_valid():
            form.save()
            messages.success(request, 'Thanks for your message!')
            return redirect('index')

        # Handle waitlist form submission
        if 'waitlist_form_submit' in request.POST and waitlist.is_valid():
            waitlist.save()
            messages.success(request, 'You have been added to the waitlist!')
            return redirect('index')
        
    else:
        form = MessageForm()
        waitlist = JoinWaitlistForm()

    return render(request, 'index.html', {'form': form, 'waitlist': waitlist})
