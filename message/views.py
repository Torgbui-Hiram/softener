from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string


# Create your views here.
from .forms import MessageForm


def send_message(request):
    sent = False
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender_mail = form.cleaned_data['sender_mail']
            message = form.cleaned_data['message']
            subj = form.cleaned_data['subj']
            receiver = 'hiramkumado@gmail.com'
            html = render_to_string(
                'som.html', {'name': name,
                             'sender_mail': sender_mail,
                             'message': message})
            send_mail(subj, message, sender_mail,
                      [receiver, ], html_message=html)
            messages.success(request, 'Message sent succesfully')
            return redirect('home')
    else:
        form = MessageForm()
        return render(request, 'contact.html', {'form': form})


def send_email(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            html = render_to_string(
                'message/emails/contact.html', {'name': name,
                                                'email': email,
                                                'message': message})
            send_mail('okito', 'This is the message', 'hiramkumado@gmail.com',
                      ['rigik11251@zuperar.com'], html_message=html)
            return redirect('send')
    else:
        form = MessageForm()
        return render(request, 'message/mailSend.html', {'form': form})
