from django.db import models
from myapp.models import Category
from django.urls import reverse

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

    # next line function will help to open particular product in single
    #  product page when we click product item(from <a> of home.html)
    def get_url(self):
        # in next line 'self' means Class Product,category means attribute of Product, and 'slug' is slug of 
        # category(this is also class in 'myapp' models) which we want to access 
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
<<<<<<< HEAD



=======
>>>>>>> 20dad98109ff5b1a447ce4de0237ad8326c2126e
    def __str__(self):
        return self.product_name