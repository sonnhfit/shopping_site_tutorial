from django.shortcuts import render
from django.views import View
from core.utils import *
from .models import Order
from django.http import HttpResponse
# Create your views here.


class CheckOutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            global_data = get_dict_home_page(request.user, -1)
            cart_id = -1
        else:
            if 'cart_id' in request.COOKIES:
                cart_id = request.COOKIES['cart_id']
            else:
                cart_id = -1
            global_data = get_dict_home_page(None, cart_id)

        response = render(request, 'homepage/checkout_view.html', {'global_data': global_data})
        set_cookie(response, 'cart_id', cart_id)

        return response

    def post(self, request):
        cart_id = request.COOKIES['cart_id']
        if request.user.is_authenticated:
            try:
                cart = Cart.objects.get(user_id=request.user.id)
            except ObjectDoesNotExist:
                return HttpResponse('đặt hàng thất bại, không tìm thấy giỏ hàng')
            name = request.POST['name']
            phone_number = request.POST['phone_number']
            shipping_address = request.POST['shipping_address']
            order_description = request.POST['order_description']
            order_object = Order.objects.create(
                user=request.user, cart=cart,
                name=name, phone_number=phone_number,
                shipping_address=shipping_address,
                order_description=order_description,
                is_completed=False
            )
            mes = 'Đơn hàng mã số %s của bạn được đặt thành công'%order_object.id
            context = {'message': mes}
            return render(request, 'homepage/success.html', context)
        else:
            try:
                cart = Cart.objects.get(id=cart_id)
            except ObjectDoesNotExist:
                return HttpResponse('đặt hàng thất bại, không tìm thấy giỏ hàng')

            name = request.POST['name']
            phone_number = request.POST['phone_number']
            shipping_address = request.POST['shipping_address']
            order_description = request.POST['order_description']
            order_object = Order.objects.create(
                user=None, cart=cart,
                name=name, phone_number=phone_number,
                shipping_address=shipping_address,
                order_description=order_description,
                is_completed=False
            )
            mes = 'Đơn hàng mã số %s của bạn được đặt thành công' % order_object.id
            context = {'message': mes}
            return render(request, 'homepage/success.html', context)
