from .models import Cart,CartItem
from carts.views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    
    else:
        try:
            cart = list(Cart.objects.filter(cart_id=_cart_id(request)).values_list('cart_id',flat=True))
            print(cart[0])
            cart_items = CartItem.objects.all().filter(cart=cart[0])
            print(cart)
            # cart_items = CartItem.objects.values('quantity')
            
            print(CartItem.objects.values('quantity'))

            for cart_item in cart_items:
                print(cart_item)
                cart_count += CartItem.quantity
                print(cart_count)
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)