from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.panel, name='panel'),
    path('admin_name_change/', views.admin_name_change, name='admin_name_change'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('logout/', views.admin_logout, name='logout'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('edit_category/<int:pk>/',views.edit_category, name='edit_category'),
    path('edit_dish/<int:pk>/',views.edit_dish, name='edit_dish'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
    path('delete_dish/<int:pk>/', views.delete_dish, name='delete_dish'),
    path('view_cat/<int:pk>', views.view_cat, name='view_cat'),
]