from django.db import models
from Pharma.models import Pharma
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='product_images/')
    pharmacy=models.ForeignKey(Pharma,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(default=1)
    

    def __str__(self):
        return self.name
