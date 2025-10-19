from django.core.paginator import Paginator
from django.shortcuts import render
from product.models import Product

def  index(request):
    query = request.GET.get('q')

    products_list = Product.objects.all().order_by('name')

    if query:
        products_list = products_list.filter(name__icontains=query)
    
    paginator = Paginator(products_list, 9)

    page_number = request.GET.get('page')

    products = paginator.get_page(page_number)

    return render(request, 'store/index.html', {'products':products, 'query': query,})
