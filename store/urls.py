from django.urls import path, include
from . import views


urlpatterns = [
    path('store/', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),

    
]
