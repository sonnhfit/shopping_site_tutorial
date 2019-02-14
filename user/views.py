from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
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
