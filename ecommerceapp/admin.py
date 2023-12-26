from django.contrib import admin
from ecommerceapp.models import Contact, Product, OrderUpdate, Order

# Register your models here.

admin.site.register(Contact) # registering Contact Info into the DB
admin.site.register(Product) # registering Product Info into the DB
admin.site.register(OrderUpdate) # registering OrderUpdate Info into the DB
admin.site.register(Order) # registering Order Info into the DB