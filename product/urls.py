from django.urls import path
from .views import ProductDetail
app_name = 'product'
urlpatterns = [
    path('detail/<int:id>', ProductDetail.as_view(), name='detail'),
]
