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
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    email = models.EmailField()
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    phone = models.CharField(max_length=50, default='')
    amount_paid = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(max_length=50, blank=True)

    def __int__(self) -> str:
        return self.order_id
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    delivered = models.BooleanField(default=False)
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)
    def __int__(self) -> str:
        return self.update_id

    def __str__(self) -> str:
        return self.update_desc[0:7] + "..."