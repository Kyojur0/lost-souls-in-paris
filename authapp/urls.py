from django.urls import path
from authapp import views as auth_views

app_name = 'authapp'

urlpatterns = [
        path('signup/', view=auth_views.handlesignup , name='signup'),
        path('login/', view=auth_views.handlelogin, name='login'),
        path('logout/', view=auth_views.handlelogout, name='logout'),
        path('activate/<uidb64>/<token>/', view=auth_views.ActivateAccountView.as_view(), name='activate'),
    ]