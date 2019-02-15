from django.shortcuts import render
from django.views import View
from product import models as product_models
# Create your views here.


class CartView(View):
    def get(self, request):
        cate = product_models.Category.objects.all()
        return render(request, 'homepage/cart_view.html',{'categorys': cate })