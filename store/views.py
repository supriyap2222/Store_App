from django.shortcuts import render,get_object_or_404
from .models import Product
from myapp.models import Category
<<<<<<< HEAD

# Create your views here.

# in line 8,category_slug is url type like url: store/battery
def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        # in next line, get_object_or_404 gives all product of particular category if != None.
        categories = get_object_or_404(Category, slug=category_slug)
        # in next line, category will be filtered with available stock.     
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    
    context = {
        'products': products,
=======
from carts.views import _cart_id
from carts.models import CartItem
from django.http import HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

# in nextline ,cat_slug is url type like url: store/battery
def store(request, cat_slug=None):
    categories = None
    products = None
    
    if cat_slug != None:
        # in next line, get_object_or_404 gives all product of particular category if != None.
        categories = get_object_or_404(Category, slug=cat_slug)
        # in next line, category will be filtered with available stock.     
        products = Product.objects.filter(category=categories, is_available=True)
        paginator =Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
# now doing code for Paginator things in 3 line ..........................................
        paginator =Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        product_count = products.count()
    
    context = {
        # 'products': products,
        'products': paged_products,

>>>>>>> 20dad98109ff5b1a447ce4de0237ad8326c2126e
        'product_count': product_count
    }

    return render(request, 'store/store.html',context)


<<<<<<< HEAD
def product_detail(request, category_slug, product_slug):
    try:
        # in next line, we need 'category_slug' i.e. inside the 'Category class' model so to access that
        # we have syntax as 'category _ _ slug' and also afterthat we need product_slug  

        single_product = Product.objects.get(category__slug=category_slug, slug = product_slug)
    except Exception as e:
        raise e    

    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)
=======
# def product_detail(request, cat_slug, prod_slug):
    # try:
    #     # in next line, we need 'cat_slug' i.e. inside the 'Category class' model so to access that
    #     # we have syntax as 'category _ _ slug' and also afterthat we need prod_slug  

    #     single_product = Product.objects.get(category__slug=cat_slug, slug = prod_slug)
    #     # single_product = Category.objects.get(product__slug=prod_slug,slug=cat_slug)
    #     print(single_product)
    #     # we are adding functionality as if product is already added or not if already added then no need to show button as 'add-to-cart-
    #     in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    #     # return HttpResponse(in_cart)
    #     # exit()
    #     # cart is foreign key inside Cart_item/ cart_id is id of class Cart inside model(carts)
    #     # also we need to import _cart_id(request)
    # except Exception as e:
    #     print(e)
    #     raise e

    # context = {
    #     'single_product': single_product,
    #     'in_cart':in_cart,
    # }

    # return render(request, 'store/product_detail.html', context)

def product_detail(request, cat_slug, prod_slug):
    single_product = Product.objects.get(category__slug=cat_slug,slug=prod_slug)
    in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
    # return HttpResponse(in_cart)

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html',context)
>>>>>>> 20dad98109ff5b1a447ce4de0237ad8326c2126e
