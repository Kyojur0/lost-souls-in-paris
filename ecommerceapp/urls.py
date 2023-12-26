from django.urls import path
from ecommerceapp import views

app_name = 'ecomapp'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('contact', view=views.contact, name='contact'),
    path('about', view=views.about, name='about'),
    path('checkout', view=views.checkout, name='checkout'),
]
