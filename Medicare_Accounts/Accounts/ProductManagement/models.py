from django.db import models
from Pharma.models import Pharma
from Patients.models import Patient
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='product_images/')
    pharmacy=models.ForeignKey(Pharma,on_delete=models.CASCADE,null=True)
    #quantity=models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.OneToOneField(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class CartItems(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)



class Order(models.Model):
    
    user=models.ForeignKey(Patient, on_delete=models.CASCADE)
    payment_status=models.CharField(max_length=20,choices=(
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
       
    ))
    status = models.CharField(max_length=20, choices=(
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ))
    total_price=models.DecimalField(max_digits=7,decimal_places=2)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    subtotal=models.DecimalField(max_digits=7,decimal_places=2)