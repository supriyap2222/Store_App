from django.db import models
from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id     = models.CharField(max_length=250, blank=True)
    date_added  = models.DateField(auto_now_add=True)
<<<<<<< HEAD

    def __str__(self):
        return self.cart_id
    
=======
    def __str__(self):
        return self.cart_id
>>>>>>> 20dad98109ff5b1a447ce4de0237ad8326c2126e
class CartItem(models.Model):
    # we should import product from store.models bcoz it is in another apps model
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart        = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity    = models.IntegerField()
    is_active   = models.BooleanField(default=True)
<<<<<<< HEAD

=======
    def sub_total(self):
        return self.product.price * self.quantity
>>>>>>> 20dad98109ff5b1a447ce4de0237ad8326c2126e
    def __str__(self):
        return self.product
    