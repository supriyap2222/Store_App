from django.shortcuts import render,redirect,HttpResponse
from store.models import Product
from .models import Cart, CartItem


#this function is made private by using _ before funct name and this is used to add product in cart without login user
def _cart_id(request):
    cart        =request.session.session_key   #session_key means session id
    if not cart:
        cart    = request.session.create()
    return cart


def add_cart(request, product_id):
    product     = Product.objects.get(id=product_id)  #get the product // product_id = single_product.id from product_detail.html page
    
    try:
        #we can add without login with help of session key 
        #session key is used as cart_id

        cart    = cart.objects.get(cart_id=_cart_id(request)) #get the cart using the _cart_id present in the sessionKey
    except cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request))      # cart_id is just session id  

    cart.save()


    #now we will combine product and cart so we can add multiple items in cart
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product, 
            quantity = 1,
            cart = cart,
            )

#CartItem is Class model inside app carts;
#cart we just created
        
        cart_item.save()
    return HttpResponse(cart_item.product)
    exit()
    return redirect('cart')


# Create your views here.
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity+= cart_item.quantity

    except OjectDoesNotExist:
        pass #just ignore
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }

    return render(request, 'store/cart.html', context)