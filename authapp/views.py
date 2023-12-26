from base64 import urlsafe_b64decode, urlsafe_b64encode
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View
from .utils import generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def handlelogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']
        try:
            user = User.objects.get(username=email)
            if user.check_password(password):
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Login Successful')
                    return redirect('/')
                else:
                    messages.warning(request, 'Account Not Activated')
                    return render(request, 'login.html')
            else:
                messages.error(request, 'Invalid Credentials')
                return render(request, 'login.html')
        except User.DoesNotExist:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')
    return render(request, 'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('authapp:login')

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            print(f'uid: {uid}, user: {user}')
        except Exception as identifier:
            user = None

        print(f'token: {generate_token.check_token(user, token)}')
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Account Activated')
            return redirect('authapp:login')
        else:
            return render(request, 'activatefail.html')

def handlesignup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']
        conf_password = request.POST['pass2']
        if password != conf_password:
            messages.warning(request, 'Passwords do not match')
            return render(request, 'signup.html')
        try:
            if User.objects.get(username=email):
                messages.warning(request, 'Email Already Exists')
                return render(request, 'signup.html')
        except Exception as identifier:
            pass

        user = User.objects.create_user(username=email, password=password, email=email)
        user.is_active = False
        user.save()

        email_subject = 'Account Activation'
        print(f'http://localhost:8000/authapp/activate/{urlsafe_base64_encode(force_bytes(user.pk))}/{generate_token.make_token(user)}')
        message = render_to_string('activate.html', {
            'user': user,
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user),
        })

        email_message = EmailMessage(
            email_subject, message, settings.EMAIL_HOST_USER, [email]
        )
        email_message.send()
        messages.success(request, 'Account Created, Please check your email to activate your account')
        return redirect('authapp:login')
    
    return render(request, 'signup.html')