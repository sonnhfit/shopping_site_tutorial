from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from product import models as product_models
# Create your views here.


class ProductDetail(View):

    def get(self, request, id):
        product = product_models.Product.objects.get(id=id)
        cate = product_models.Category.objects.all()
        context = {'categorys': cate, 'product': product}
        return render(request, 'homepage/product_view.html', context)