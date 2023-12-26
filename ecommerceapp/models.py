from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images', default='')
    
    def __str__(self) -> str:
        return self.product_name
    
class Order(models.Model):

    def __int__(self) -> str:
        return self.order_id
    
class OrderUpdate(models.Model):

    def __int__(self) -> str:
        return self.update_id