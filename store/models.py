from django.db import models
from myapp.models import Category

# Create your models here.
class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    other_name    = models.CharField(max_length=200, null=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    mrp             = models.IntegerField(null=True)
    price           = models.IntegerField()
    cp_code         = models.CharField(max_length=20, null=True)
    image           = models.ImageField(upload_to='photos/product',blank=True)
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now=True)
    modified_date    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name