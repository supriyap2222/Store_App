from django.urls import path, include
from . import views


urlpatterns = [
    path('store/', views.store, name='store'),
    path('<slug:cat_slug>/', views.store, name='products_by_category'),
    path('<slug:cat_slug>/<slug:prod_slug>/', views.product_detail, name='product_detail'),


    
]
