from django.urls import path
from .views import CartView, AddCartAPIView, DelCartItem
app_name = 'cart'
urlpatterns = [
    path('view/', CartView.as_view(), name='view_cart'),
    path('add/', AddCartAPIView.as_view(), name='add_cart'),
    path('del/', DelCartItem.as_view(), name='del_cart'),
]