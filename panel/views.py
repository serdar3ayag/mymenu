from django.shortcuts import render, loader, redirect, get_object_or_404
from .models import Category, Dish
from django.http import HttpResponse, JsonResponse
from .templates import *
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AdminChangeForm, AdminLoginForm, CategoryForm, DishForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#adding objects to panel

def add_category(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('panel') 
        else:
            form = CategoryForm()
        return render(request, 'add_category.html', {'form': form})
    else:
        return redirect('sign_in') 


def add_dish(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = DishForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('panel') 
        else:
            form = DishForm()
        return render(request, 'add_dish.html', {'form': form})
    else:
        return redirect('sign_in')    


#editing and deleting objects
def edit_category(request, pk):
    if request.user.is_authenticated:
        categ = get_object_or_404(Category, pk=pk)
        if request.method == "POST":
            form = CategoryForm(request.POST, request.FILES, instance=categ)
            if form.is_valid():
                form.save()
                return redirect('panel')
        else:
            form = CategoryForm()
        return render(request, 'edit_category.html', {'form': form}) 
    else:
        return redirect('sign_in')    


def edit_dish(request, pk):
    if request.user.is_authenticated:
        dish = get_object_or_404(Dish, pk=pk)
        if request.method == "POST":
            form = DishForm(request.POST, instance=dish)
            if form.is_valid():
                form.save()
                return redirect('panel')
        else:
            form = DishForm(instance=dish)
        return render(request, 'edit_dish.html', {'form': form})
    else:
        return redirect('sign_in')    


def delete_category(request, pk):
    if request.user.is_authenticated:
        categ = get_object_or_404(Category, pk=pk)
        categ.delete()
        return redirect('panel')
    else:
        return redirect('sign_in')    


def delete_dish(request, pk):
    if request.user.is_authenticated:
        dish = get_object_or_404(Dish, pk=pk)
        dish.delete()
        return redirect('panel')
    else:
        return redirect('sign_in')    
 



#admin panel itself

def panel(request):
    if request.user.is_authenticated:
        user = User.objects.get(is_superuser=True)
        Categories = Category.objects.all()
        Dishes = Dish.objects.all()
        context = {
            'user': user,
            'categories': Categories,
            'dishes' : Dishes,
        }
        return render(request, 'panel.html', context)
    else:
        return redirect('sign_in') 


#changing admin's data

def admin_name_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AdminChangeForm(request.POST)
            if form.is_valid():
                new_name = form.cleaned_data['new_name']
                new_password = form.cleaned_data['new_password']
                user = User.objects.get(is_superuser=True)

                if new_name:
                    user.username = new_name

                if new_password:
                    user.set_password(new_password)

                user.save()
                messages.success(request, 'Admin changed')
                return redirect('/panel')
        else:
            form = AdminChangeForm()
        return render(request, 'sign_up.html', {'form' : form})
    else:
        return redirect('sign_in')

#logging in as admin

def sign_in(request):
    if request.method == 'POST':
        form = AdminLoginForm(request ,data=request.POST)
        if form.is_valid():
            user = User.objects.get(is_superuser=True)
            if user.is_authenticated:
                login(request, user)
                return redirect('panel')
            else:
                messages.error(request, 'Only admin allowed')
    else:
        form = AdminLoginForm()
    return render(request, 'sign_in.html', {'form' : form})    
            

#logout

def admin_logout(request):
    logout(request)
    return redirect('sign_in')


#view categories


def view_cat(request, pk):
    if request.user.is_authenticated:
        cat = get_object_or_404(Category, pk=pk)
        dishes = cat.dish_set.all()
        context = {
            'cat' : cat,
            'dishes' : dishes,
        }
        return render(request, 'view_cat.html', context)
    else:
        return redirect('sign_in')
    