from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path("add/", views.add_department, name='add_department'),
    path('edit/<int:id>/', views.edit_department, name='edit_department'),
    path('delete/<int:id>/', views.delete_department, name='delete_department'),
]
