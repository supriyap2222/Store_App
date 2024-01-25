from django.urls import path
from . import views


urlpatterns = [
    path('',views.cart, name='cart'),
<<<<<<< HEAD
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart')
=======
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    # below line url is to reduce the quantity of product
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    # below line is to delete the product
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),

>>>>>>> 20dad98109ff5b1a447ce4de0237ad8326c2126e

]
