from django.urls import path
from .views import *
app_name = 'order'
urlpatterns = [
    path('checkout/', CheckOutView.as_view(), name='checkout'),

]