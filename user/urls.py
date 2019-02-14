from django.urls import path
from .views import LoginView, UserRegister
app_name = 'user'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserRegister.as_view(), name='register')
]
