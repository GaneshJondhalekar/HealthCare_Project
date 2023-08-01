from django.contrib import admin

# Register your models here.
from .models import Product,CartItems,Cart
# Register your models here.
admin.site.register(Product)
admin.site.register(CartItems)