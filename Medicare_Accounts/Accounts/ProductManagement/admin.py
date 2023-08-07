from django.contrib import admin

# Register your models here.
from .models import Product,CartItems,Cart,Order,OrderItem
# Register your models here.
admin.site.register(Product)
admin.site.register(CartItems)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)