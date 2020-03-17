from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=200)
    password1 = forms.CharField(max_length=200)
    password2 = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=200)
    las_name = forms.CharField(max_length=200)
    fis_name = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)