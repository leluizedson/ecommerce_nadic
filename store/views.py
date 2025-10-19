from django.core.paginator import Paginator
from django.shortcuts import render
from product.models import Product

def  index(request):
    products_list = Product.objects.all().order_by('name')

    paginator = Paginator(products_list, 9)

    page_number = request.GET.get('page')

    products = paginator.get_page(page_number)

    return render(request, 'store/index.html', {'products':products})
