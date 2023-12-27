from base64 import urlsafe_b64decode, urlsafe_b64encode
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View
from .utils import generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# Create your views here.
def handlelogin(request):
    """
    This function handles the login request.
    Parameters:
        request (HttpRequest): The request object.
    Returns:
        HttpResponse: The response object.
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']
        try:
            user = User.objects.get(username=email)
            if user.check_password(password):
                if user.is_active:
                    login(request, user) # this line keeps track of each user thru `request`
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
    logout(request) # removes the track for user for specific use-cases 
    messages.success(request, 'Logout Successful')
    return redirect('authapp:login') # redirects to domain/authapp/login 

class ActivateAccountView(View):
    """
    View class for activating user accounts.

    This view is responsible for activating user accounts by verifying the activation token
    and setting the user's `is_active` flag to True.

    Attributes:
        - None

    Methods:
        - get(request, uidb64, token): Handles the GET request for activating the user account.

    Usage:
        - Create an instance of this class and map it to a URL pattern in your Django project's
          URL configuration file to handle the activati on process.

    Example:
        ```
        from django.urls import path
        from .views import ActivateAccountView

        urlpatterns = [
            path('activate/<str:uidb64>/<str:token>/', ActivateAccountView.as_view(), name='activate'),
        ]
        ```

    """
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Account Activated')
            return redirect('authapp:login')
        else:
            return render(request, 'activatefail.html')

def handlesignup(request):
    """
    Handles the signup process for a user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        None

    Notes:
        This function is responsible for processing the signup form submitted by the user.
        It validates the form data, creates a new user account, sends an activation email,
        and redirects the user to the login page.

        The function expects a POST request with the following parameters in the request body:
        - email: The email address of the user.
        - pass1: The password entered by the user.
        - pass2: The password confirmation entered by the user.

        If the passwords do not match, a warning message is displayed and the user is redirected
        back to the signup page.

        If the email address already exists in the database, a warning message is displayed and
        the user is redirected back to the signup page.

        If the form data is valid, a new user account is created with the provided email and password.
        The account is set to inactive until the user activates it by clicking on the activation link
        sent to their email address.

        An activation email is sent to the user's email address with a unique activation link.
        The activation link contains a token that is used to verify the user's identity.

        After the account is created and the activation email is sent, a success message is displayed
        and the user is redirected to the login page.

        If the request method is not POST, the signup page is rendered.

    """
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

        # < SENDING EMAIL WITH ACCOUNT ACTIVATION LINK > # 

        email_subject = 'Account Activation'
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

def handlereset(request):
    """
    Handles the password reset process for a user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        None

    Notes:
        This function is responsible for processing the password reset form submitted by the user.
        It validates the form data, creates a new password reset token, sends an email with the
        password reset link to the user's email address, and redirects the user to the login page.

        The function expects a POST request with the following parameters in the request body:
        - email: The email address of the user.

        If the email address does not exist in the database, a warning message is displayed and
        the user is redirected back to the password reset page.

        If the form data is valid, a new password reset token is created and emailed to the user.
        The email contains a link to a password reset page where the user can enter a new password.

        After the email is sent, a success message is displayed and the user is redirected to the login page.

        If the request method is not POST, the password reset page is rendered.

    """
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(username=email)
        except Exception as identifier:
            messages.warning(request, 'Email does not exist')
            return redirect('authapp:reset_password')

        email_subject = 'Password Reset'
        message = render_to_string('reset-user-password.html', {
            'user': user,
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user),
        })

        email_message = EmailMessage(
            email_subject, message, settings.EMAIL_HOST_USER, [email]
        )
        email_message.send()
        messages.success(request, 'Password Reset Email Sent')
        return redirect('authapp:login')
    
    
    return render(request, 'request-reset-email.html')

class RequestResetEmailView(View):
    """
        RequestResetEmailView handles the submission of the 'Forgot Password' form,
        where users provide their email address for a password reset.

        Methods:
        - get: Renders the 'request-reset-email.html' template for the GET request.
        - post: Processes the POST request, validates the email, sends a password
                reset email, and redirects the user accordingly.

        Attributes:
        - template_name (str): The name of the HTML template to render for the GET request.
    """
    def get(self, request):
        """
        Handles GET requests for the 'Forgot Password' form.

        Returns:
        - Rendered HTML response displaying the 'request-reset-email.html' template.
        """
        return render(request, 'request-reset-email.html')
    
    def post(self, request):
        """
        Handles POST requests for the 'Forgot Password' form.

        Parameters:
        - request (HttpRequest): The HTTP request object containing form data.

        Returns:
        - Redirects the user based on the result of the password reset email operation.
        """
        email = request.POST['email']
        try:
            user = User.objects.get(username=email)
        except Exception as identifier:
            messages.warning(request, 'Email does not exist')
            return redirect('authapp:reset_password')
        
        email_subject = 'Password Reset'
        message = render_to_string('reset-user-password.html', {
            'user': user,
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': PasswordResetTokenGenerator().make_token(user),
        })

        email_message = EmailMessage(
            email_subject, message, settings.EMAIL_HOST_USER, [email]
        )

        email_message.send()
        messages.success(request, 'Password Reset Email Sent')
        return redirect('authapp:login')
    
class SetNewPasswordView(View):
    def get(self,request,uidb64,token):
        """
        This function handles the GET request for activating the user account.

        Parameters:
            request (HttpRequest): The request object.
            uidb64 (str): The base64-encoded user ID.
            token (str): The activation token.

        Returns:
            HttpResponse: The response object.

        Raises:
            None

        Notes:
            If the activation token is valid, the user's account is activated and they are redirected
            to the login page. If the token is invalid, an error message is displayed.

        """
        context = {
            'uidb64':uidb64,
            'token':token
        }
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=user_id)

            if  not PasswordResetTokenGenerator().check_token(user,token):
                messages.warning(request,"Password Reset Link is Invalid")
                return redirect('authapp:reset_password')

        except DjangoUnicodeDecodeError as identifier:
            pass

        return render(request,'set-new-password.html',context)

    def post(self,request,uidb64,token):
        """
        Handles the submission of the 'Set New Password' form,
        where users provide their new password after resetting their password.

        Parameters:
        request (HttpRequest): The HTTP request object containing form data.
        uidb64 (str): The base64-encoded user ID.
        token (str): The password reset token.

        Returns:
        HttpResponse: A redirect to the login page if the password reset is successful,
        or a rendered HTML response displaying the 'set-new-password.html' template
        with error messages if the password reset is unsuccessful.

        """
        context={
            'uidb64':uidb64,
            'token':token
        }
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'set-new-password.html',context)
        
        try:
            user_id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            messages.success(request,"Password Reset Success Please Login with NewPassword")
            return redirect('authapp:login')

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request,"Something Went Wrong")
            return render(request,'set-new-password.html',context)

        return render(request,'set-new-password.html',context)
