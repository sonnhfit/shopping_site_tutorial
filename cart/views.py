from django.shortcuts import render
from django.views import View
from product import models as product_models
from core.utils import *
# Create your views here.


class CartView(View):
    def get(self, request):
        global_data = get_dict_home_page(request.session.session_key)
        return render(request, 'homepage/cart_view.html',{'global_data': global_data})