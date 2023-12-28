from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Category,Dish

class AdminChangeForm(forms.ModelForm):
    new_name = forms.CharField(required=False)
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['new_name', 'new_password']


class AdminLoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_ru', 'name_en', 'image']


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name_en', "name_ru",'Category', 'price']