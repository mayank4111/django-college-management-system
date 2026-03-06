from django.urls import path
from .views import DepartmentListView, AddDepartmentView, EditDepartmentView, DeleteDepartmentView

urlpatterns = [
    path('', DepartmentListView.as_view(), name='department_list'),
    path('add/', AddDepartmentView.as_view(), name='add_department'),
    path('edit/<int:id>/', EditDepartmentView.as_view(), name='edit_department'),
    path('delete/<int:id>/', DeleteDepartmentView.as_view(), name='delete_department'),
]