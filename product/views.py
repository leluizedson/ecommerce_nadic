from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    latest_product_list = Product.objects.order_by('-stock')
    context = {
        'latest_product_list': latest_product_list
        }
    return render(request, 'product/index.html', context)

def detail(request, product_id):
    return HttpResponse("This is the product formerly known as: %s" % product_id)
