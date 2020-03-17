from django.shortcuts import render, redirect
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


class ViewCategory(View):
    def get(self, request, slug):
        try:
            cate = product_models.Category.objects.get(slug=slug)
        except ObjectDoesNotExist:
            return redirect('core:index')

        product_id = product_models.Product.objects.filter(
            category=cate
        ).values_list('id', flat=True)

        vari = product_models.Variation.objects.filter(
            product_id__in=product_id
        )
        if request.user.is_authenticated:
            global_data = get_dict_home_page(request.user, -1)
            cart_id = -1
        else:
            if 'cart_id' in request.COOKIES:
                cart_id = request.COOKIES['cart_id']
            else:
                cart_id = -1
            global_data = get_dict_home_page(None, cart_id)

        response = render(request, 'homepage/view_cate_product.html', {'global_data': global_data, 'variation': vari, 'cates': cate})
        set_cookie(response, 'cart_id', cart_id)
        return response