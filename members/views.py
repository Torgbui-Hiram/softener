from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from product.models import Traders, FabricSoftener


from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from django.conf.global_settings import EMAIL_HOST_USER

# user registration and authentication


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product-view')
        else:
            messages.success(
                request, 'There was a problem login in! try again')
    return render(request, 'login.html', {})


# logout
def signout(request):
    logout(request)
    return redirect('home')
# register user


def register_user(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # save form in the memory not in database
            email = request.POST['email']
            from_mail = EMAIL_HOST_USER
            receipient_list = [email]
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(mail_subject, message, from_mail,
                      receipient_list, fail_silently=False)
            return HttpResponse('Please confirm your email address to complete the registration')

    else:
        form = SignupForm()
    return render(request, 'register.html', {})

# activate mail


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request,
            "Thank you for your email confirmation. Now you can login to your account.",)
        return redirect('user_login')
    else:
        return HttpResponse('Activation link is invalid!')



