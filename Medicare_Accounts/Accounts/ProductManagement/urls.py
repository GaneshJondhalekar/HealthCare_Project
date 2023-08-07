"""Accounts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import ProductAddView,ProductListView,ProductDetailView,AddProductToCartView,MyCartView,PlaceOrderView,MyOrdersView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'orders',MyOrdersView,basename='orders')
urlpatterns = [
   path('add/',ProductAddView.as_view(),name='add_product'),
   path('lists/',ProductListView.as_view(),name='list_product'),
   path('list/<int:id>/',ProductDetailView.as_view(),name='product_details'),
   path('addTocart/',AddProductToCartView.as_view(),name='add_cart'),
   path('mycart/',MyCartView.as_view(),name='my_cart'),
   path('mycart/<int:id>/',AddProductToCartView.as_view(),name='cartitem_details'),
   path('place_order/',PlaceOrderView.as_view(),name='place_order'),
   path('myorders/',include(router.urls))
]
