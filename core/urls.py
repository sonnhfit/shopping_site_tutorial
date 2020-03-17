from django.urls import path
from .views import HomeView, ViewCategory
app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('cate/<slug>/', ViewCategory.as_view(), name='cate_view'),
]
