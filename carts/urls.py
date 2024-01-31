from django.urls import path
from . import views


urlpatterns = [
    path('',views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    # below line url is to reduce the quantity of product
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    # below line is to delete the product
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),


]
