from django.urls import path, include
from . import views


urlpatterns = [
    path('store/', views.store, name='store'),
<<<<<<< HEAD
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
=======
    path('<slug:cat_slug>/', views.store, name='products_by_category'),
    path('<slug:cat_slug>/<slug:prod_slug>/', views.product_detail, name='product_detail'),
>>>>>>> 20dad98109ff5b1a447ce4de0237ad8326c2126e


    
]
