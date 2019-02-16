from product.models import Category, Variation
from cart.models import Cart, CartItem
from cart.utils import *


def get_dict_home_page(ss_key):
    cate = Category.objects.all()
    cart_count = get_count_cart(ss_key)
    return {'categorys': cate, 'cart_count': cart_count}