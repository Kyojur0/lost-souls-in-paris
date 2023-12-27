from django.urls import path
from authapp import views as auth_views

app_name = 'authapp'

urlpatterns = [
        path('signup/', view=auth_views.handlesignup , name='signup'),
        path('login/', view=auth_views.handlelogin, name='login'),
        path('logout/', view=auth_views.handlelogout, name='logout'),
        path('activate/<uidb64>/<token>/', 
             view=auth_views.ActivateAccountView.as_view(), 
             name='activate'), # this `/<uidb64>/<token>/` means that we are going 
            # to encounter some random values and let them called "uidb64" and "token"
            # and since the implementation of this endpoint is based on "class" it will handle
            # both GET & POST requests on this URL path.
        path('request-reset-email/', 
             view=auth_views.RequestResetEmailView.as_view(), 
             name='reset_password'),
        path('set-new-password/<uidb64>/<token>/', 
             view=auth_views.SetNewPasswordView.as_view(), 
             name='password_confirm'),
    ]