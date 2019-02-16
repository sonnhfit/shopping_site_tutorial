from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


def get_cart_id_from_ss_key(user_id):
    try:
        cart = Cart.objects.get(user_id=user_id)
    except ObjectDoesNotExist:
        return 0

    return cart.id


def get_count_cart(user_id):
    cart_id = get_cart_id_from_ss_key(user_id)
    if cart_id == 0:
        return 0
    return CartItem.objects.filter(cart_id=cart_id).count()


def get_count_cart_use_cart_id(cart_id):
    if cart_id == -1:
        return 0
    return CartItem.objects.filter(cart_id=cart_id).count()


def get_total_price_cart_anonymous(cart_id):
    cart_items = CartItem.objects.filter(cart_id=cart_id)
    total_price = 0
    for item in cart_items:
        total_price += (item.quantity*item.item.price)
    return total_price


def get_total_price_cart_with_user_id(user_id):
    cart_id = get_cart_id_from_ss_key(user_id)
    total_price = get_total_price_cart_anonymous(cart_id)
    return total_price
