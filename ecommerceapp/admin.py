from django.contrib import admin
from ecommerceapp.models import Contact, Product, OrderUpdate, Order

# Register your models here.
"""
    This file is responsible for registering the models in the Django admin site.
    It imports the necessary models from the ecommerceapp.models module and registers 
    them using the admin.site.register() function. Each model is registered to allow 
    it to be managed through the Django admin interface.
"""
admin.site.register(Contact) # registering Contact Info into the DB
admin.site.register(Product) # registering Product Info into the DB
admin.site.register(OrderUpdate) # registering OrderUpdate Info into the DB
admin.site.register(Order) # registering Order Info into the DB

