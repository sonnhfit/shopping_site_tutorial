from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=200)
    password1 = forms.CharField(max_length=200)
    password2 = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)