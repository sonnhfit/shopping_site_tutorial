from django.shortcuts import render
from django.views import View
from product import models as product_models
from .utils import *
# Create your views here.


class HomeView(View):
    def get(self, request):
        global_data = get_dict_home_page(request.session.session_key)
        variation = product_models.Variation.objects.all()[:6]
        return render(request, 'homepage/index.html', {'global_data': global_data, 'variation': variation})