# Generated by Django 3.2.20 on 2023-08-01 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManagement', '0003_cart_cartitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
