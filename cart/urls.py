from django.urls import path
from .views import CartView
app_name = 'cart'
urlpatterns = [
    path('view/', CartView.as_view(), name='view_cart'),
]