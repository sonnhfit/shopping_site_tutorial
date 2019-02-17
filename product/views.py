from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from product import models as product_models
from core.utils import *
# Create your views here.


class ProductDetail(View):

    def get(self, request, id):
        variation = product_models.Variation.objects.get(id=id)

        if request.user.is_authenticated:
            global_data = get_dict_home_page(request.user, -1)
            cart_id = -1
        else:
            if 'cart_id' in request.COOKIES:
                cart_id = request.COOKIES['cart_id']
                print(cart_id)
            else:
                cart_id = -1
            global_data = get_dict_home_page(None, cart_id)

        context = {'global_data': global_data, 'variation': variation}
        return render(request, 'homepage/product_view.html', context)