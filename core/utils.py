from product.models import Category, Variation
from cart.models import Cart, CartItem
from cart.utils import *
import datetime


def get_dict_home_page(user_id=None, cart_id=-1):
    cate = Category.objects.all()
    if user_id is None and cart_id == -1:
        cart_count = 0
        total_price = 0
    if user_id:
        cart_count = get_count_cart(user_id)
        total_price = get_total_price_cart_with_user_id(user_id)
    if cart_id != -1:
        cart_count = get_count_cart_use_cart_id(cart_id)
        total_price = get_total_price_cart_anonymous(cart_id)

    return {'categorys': cate, 'cart_count': cart_count, 'total_price': total_price, 'cart_id': cart_id}


def set_cookie(response, key, value, days_expire = 7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires, domain='mysite', secure=None)