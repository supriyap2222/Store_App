from django.shortcuts import render,get_object_or_404
from .models import Product
from myapp.models import Category

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
        'product_count': product_count
    }

    return render(request, 'store/store.html',context)


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
