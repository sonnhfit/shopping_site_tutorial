from django.shortcuts import render
from django.views import View
from product import models as product_models
from core.utils import *
# Create your views here.


class CartView(View):
    def get(self, request):
        ss_key = request.session.session_key
        cart_id = get_cart_id_from_ss_key(ss_key)
        global_data = get_dict_home_page(ss_key)
        cart_item = CartItem.objects.filter(cart_id=cart_id)
        context = {'global_data': global_data, 'cart_item': cart_item}
        return render(request, 'homepage/cart_view.html', context)