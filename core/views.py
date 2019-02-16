from django.shortcuts import render
from django.views import View
from product import models as product_models
# Create your views here.


class HomeView(View):
    def get(self, request):
        cate = product_models.Category.objects.all()
        variation = product_models.Variation.objects.all()[:6]
        return render(request, 'homepage/index.html', {'categorys': cate, 'variation': variation})