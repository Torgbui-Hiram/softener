from django import forms
from datetime import datetime


class MessageForm(forms.Form):
    subj = forms.CharField(max_length=250)
    name = forms.CharField(max_length=60)
    sender_mail = forms.EmailField(max_length=150)
    message = forms.CharField(max_length=1000)

    # sending_time = datetime.date()
    # time = forms.DateTimeInput()
