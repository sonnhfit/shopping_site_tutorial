from django.shortcuts import render
from django.views import View
from product import models as product_models
from core.utils import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import *
from django.contrib.sessions.models import Session
# Create your views here.


class CartView(View):
    def get(self, request):
        user_id = request.user.id

        if request.user.is_authenticated:
            cart_id = get_cart_id_from_ss_key(user_id)
            global_data = get_dict_home_page(user_id, cart_id)
            cart_item = CartItem.objects.filter(cart_id=cart_id)
            context = {'global_data': global_data, 'cart_item': cart_item}
            return render(request, 'homepage/cart_view.html', context)
        else:
            if 'cart_id' in request.COOKIES:
                cart_id = request.COOKIES['cart_id']
            else:
                cart_id = -1
            global_data = get_dict_home_page(user_id, cart_id)
            cart_item = CartItem.objects.filter(cart_id=cart_id)
            context = {'global_data': global_data, 'cart_item': cart_item}
            return render(request, 'homepage/cart_view.html', context)


class AddCartAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        valid = AddCartItemSerializer(data=request.data)
        if not valid.is_valid():
            return Response('not valid data', status=status.HTTP_400_BAD_REQUEST)
        item_id = valid.data['item_id']
        quantity = valid.data['quantity']
        cart_id = valid.data['cart_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            try:
                cart = Cart.objects.get(user_id=user_id)
            except ObjectDoesNotExist:
                cart = Cart.objects.create(user_id=user_id)
            varia = product_models.Variation.objects.get(id=item_id)
            CartItem.objects.create(cart=cart, quantity=quantity, item=varia)
            return Response(cart.id, status=status.HTTP_200_OK)

        else:
            if cart_id == -1:
                cart = Cart.objects.create(user=None)
                varia = product_models.Variation.objects.get(id=item_id)
                cart_item = CartItem.objects.create(cart=cart, item=varia, quantity=quantity)
                return Response(cart.id, status=status.HTTP_200_OK)
            else:
                try:
                    cart = Cart.objects.get(id=cart_id)
                except ObjectDoesNotExist:
                    return Response('bad request', status=status.HTTP_400_BAD_REQUEST)
                varia = product_models.Variation.objects.get(id=item_id)
                CartItem.objects.create(cart=cart, item=varia, quantity=quantity)
                return Response(cart.id, status=status.HTTP_200_OK)
            # if cart_id == -1:
            #     cart = Cart.objects.create(user=None)
            #     varia = product_models.Variation.objects.get(id=item_id)
            #     CartItem.objects.create(cart=cart, item=varia, quantity=quantity)
            #     cart_sertial = CartSerializer(data=cart)
            #
            #     return Response(data=cart_sertial.data, status=status.HTTP_200_OK)
            # else:

            # try:
            #     cart = Cart.objects.get(id=cart_id)
            # except ObjectDoesNotExist:
            #     return Response('bad request', status=status.HTTP_400_BAD_REQUEST)
            #
            # varia = product_models.Variation.objects.get(id=item_id)
            # CartItem.objects.create(cart=cart, item=varia, quantity=quantity)
            # cart_sertial = CartSerializer(data=cart)
            # return Response(cart_sertial.data, status=status.HTTP_200_OK)
