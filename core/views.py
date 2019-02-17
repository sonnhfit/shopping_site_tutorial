from django.shortcuts import render
from django.views import View
from product import models as product_models
from .utils import *
# Create your views here.


class HomeView(View):
    def get(self, request):
        variation = product_models.Variation.objects.all()[:6]
        if request.user.is_authenticated:
            global_data = get_dict_home_page(request.user, -1)
            cart_id = -1
        else:
            if 'cart_id' in request.COOKIES:
                cart_id = request.COOKIES['cart_id']
            else:
                cart_id = -1
            global_data = get_dict_home_page(None, cart_id)

        response = render(request, 'homepage/index.html', {'global_data': global_data, 'variation': variation})
        set_cookie(response, 'cart_id', cart_id)
        return response
