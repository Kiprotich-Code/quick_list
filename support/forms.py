from django import forms
from .models import MessageList, WaitList

class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageList
        fields = '__all__'


class JoinWaitlistForm(forms.ModelForm):
    class Meta:
        model = WaitList
        fields = '__all__'
