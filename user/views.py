from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import CustomerUser
# Create your views here.


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:index')
        return render(request, 'homepage/login.html')

    def post(self, request):
        username = request.POST['uname']
        password = request.POST['psw']

        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('dang nhap khong thanh cong')

        login(request, user)
        return redirect('core:index')


class UserRegister(View):

    def get(self, request):
        fm = UserForm()
        return render(request, 'homepage/register.html', {'fm': fm})

    def post(self, request):
        fm = UserForm(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            pas1 = fm.cleaned_data['password1']
            pas2 = fm.cleaned_data['password2']
            email = fm.cleaned_data['email']
            if pas1 == pas2:
                CustomerUser.objects.create_user(username=username, password=pas1, email=email)
                return HttpResponse('dang ky thanh cong')
            else:
                return HttpResponse('password not valid')

        return HttpResponse('form not valid')