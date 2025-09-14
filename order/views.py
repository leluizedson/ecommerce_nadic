from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from .models import Order, OrderItem

@login_required(login_url='register')
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    if not items:
        return redirect('index')

    total = sum(item.total_price() for item in items)

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total=total)

        for item in items:
            OrderItem.objects.create(
                order=order,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price
            )
        items.delete()
        return redirect('order_confirmation', order_id=order.id)
    return render ( request, 'order/checkout.html', {'items': items, 'total': total})

@login_required(login_url='register')
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'order/confirmation_order.html', {'order': order})