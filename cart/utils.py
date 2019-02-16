from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


def get_cart_id_from_ss_key(ss_key):
    try:
        cart = Cart.objects.get(session_key=ss_key)
    except ObjectDoesNotExist:
        return 0

    return cart.id

def get_count_cart(ss_key):
    cart_id = get_cart_id_from_ss_key(ss_key)
    if cart_id == 0:
        return 0
    return CartItem.objects.filter(cart_id=cart_id).count()


def get_total_price_cart(ss_key):
    cart_id = get_cart_id_from_ss_key(ss_key)
    cart_items = CartItem.objects.filter(cart_id=cart_id)
    total_price = 0
    for item in cart_items:
        total_price += (item.quantity*item.item.price)

    return total_price