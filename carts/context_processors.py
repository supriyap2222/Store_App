from .models import Cart,CartItem
from carts.views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    
    else:
        try:
            cart = list(Cart.objects.filter(cart_id=_cart_id(request)).values_list('id',flat=True))
            if cart:
                # print(cart)
                cart_items = CartItem.objects.filter(cart_id = cart[0]).values('quantity')
            
                for cart_item in cart_items:
                    cart_count += cart_item['quantity']
            else:
                pass
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)