from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='register')
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = sum(item.total_price() for item in items)

    out_of_stock = any(item.quantity > item.product.stock for item in items)

    return render(request, 'cart/cart.html', {'items': items, 'total': total, 'out_of_stock': out_of_stock})

@login_required(login_url='register')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if item.quantity >= product.stock:
        messages.error(request, f"Estoque insuficiente para {product.name}.")
        return redirect('cart_view')
    
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart_view')

@login_required(login_url='register')
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity < item.product.stock:
        item.quantity += 1
        item.save()
    else:
        messages.error(request, f"Estoque insuficiente para {item.product.name}.")

    return redirect('cart_view')


# ➖ DIMINUIR 1 unidade
@login_required(login_url='register')
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()  # se chegar a zero, remover do carrinho

    return redirect('cart_view')


@login_required(login_url='register')
def delete_from_cart(request, product_id):
    item = get_object_or_404(CartItem, id=product_id)
    item.delete()
    return redirect('cart_view')
