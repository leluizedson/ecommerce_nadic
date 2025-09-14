from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    latest_product_list = Product.objects.order_by('-stock')
    context = {
        'latest_product_list': latest_product_list
        }
    return render(request, 'product/index.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/product_detail.html', {'product': product})