from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

#this function is made private by using _ before funct name and this is used to add product in cart without login user
def _cart_id(request):
    cart        =request.session.session_key   #session_key means session id
    if not cart:
        cart    = request.session.create()
    return cart


def add_cart(request, product_id):
    
    color = request.POST.get('color')
    print(color)
    size = request.POST.get('size')
    print(size)
    return HttpResponse(color)
    exit()
    
    product     = Product.objects.get(id=product_id)  #get the product // product_id = single_product.id from product_detail.html page
    print('product id', product_id)
    try:
        #we can add without login with help of session key 
        #session key is used as cart_id
        cart    =  Cart.objects.get(cart_id=_cart_id(request)) #get the cart using the _cart_id present in the sessionKey
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request))      # cart_id is just session id  
    cart.save()


    #now we will combine product and cart so we can add multiple items in cart
    # also this is funtc for adding in add-to-cart page
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
        cart_item.save()
    return redirect('cart')
#CartItem is Class model inside app carts;
#cart we just created
        
        # to reduce using - button in cart page
def remove_cart(request,product_id):

    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = Product.objects.get(id=product_id)
    print('product id', product_id)

    # product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()    
    else: 
        cart_item.delete()
    return redirect('cart')
# this will redirect to cart.html page


# to delete the product form cart-page
def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    # product = get_object_or_404(Product, id=product_id)
    product = Product.objects.get(id=product_id)
    cart_item = CartItem.objects.get(cart=cart,product=product)
    print('Deleted Product ID:',product_id)

    cart_item.delete()
    return redirect('cart')

# Create your views here.
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = 0
        delivery = 100
        grand_total = total + tax + delivery
    
    except ObjectDoesNotExist:
        pass
    
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return render(request, 'store/cart.html', context)