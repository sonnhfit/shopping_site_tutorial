from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from product import models as product_models
from core.utils import *
# Create your views here.


class ProductDetail(View):

    def get(self, request, id):
        variation = product_models.Variation.objects.get(id=id)
        global_data = get_dict_home_page(request.session.session_key)
        context = {'global_data': global_data, 'variation': variation}
        return render(request, 'homepage/product_view.html', context)