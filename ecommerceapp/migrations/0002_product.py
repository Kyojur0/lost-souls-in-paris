# Generated by Django 5.0 on 2023-12-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('subcategory', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(default='', upload_to='images/images')),
            ],
        ),
    ]