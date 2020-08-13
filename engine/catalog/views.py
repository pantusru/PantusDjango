from .models import *
# Create your views here.

def getiing(request):
    print('sdfdssdfsdfsdfsdf')
    #print(Product.objects.filter(category_id__in=ProductCategory.objects.get(id=3009).get_descendants(include_self=True)))


    categories = ProductCategory.objects.prefetch_related('category_products')


    stores = []
    for cat in categories:
        products = [{'product_id':  product.id, 'product_name':  product.name} for product in cat.get_products()]

        if not products:
            pass
        else:
            stores.append({'category_id': cat.id, 'category_name': cat.name, 'products': products})
    print(stores)
