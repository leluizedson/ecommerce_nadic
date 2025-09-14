from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from product.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='register')
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = sum(item.total_price() for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})

@login_required(login_url='register')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart_view')

@login_required(login_url='register')
def delete_from_cart(request, product_id):
    item = get_object_or_404(CartItem, id=product_id)
    item.delete()
    return redirect('cart_view')
