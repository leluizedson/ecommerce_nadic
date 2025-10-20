from django.core.paginator import Paginator
from django.shortcuts import render
from product.models import Product

def  index(request):
    query = request.GET.get('q')

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    products_list = Product.objects.all().order_by('name')

    if query:
        products_list = products_list.filter(name__icontains=query)

    if min_price:
        products_list = products_list.filter(price__gte=min_price)
    if max_price:
        products_list = products_list.filter(price__lte=max_price)

    paginator = Paginator(products_list, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'store/index.html', {'products':products, 'query': query, 'min_price': min_price,
        'max_price': max_price,})
