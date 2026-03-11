from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Dept_Details
from .forms import DeptForm


# View Departments (Login Required)
class DepartmentListView(LoginRequiredMixin, ListView):
    model = Dept_Details
    template_name = 'Department/department_list.html'
    context_object_name = 'departments'


# Add Department (Admin - Add Permission)
class AddDepartmentView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Dept_Details
    form_class = DeptForm
    template_name = 'Department/add_department.html'

    success_url = reverse_lazy('department_list')
    permission_required = 'Department.add_dept_details'


# Edit Department (Staff + Admin - Change Permission)
class EditDepartmentView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Dept_Details
    form_class = DeptForm
    template_name = 'Department/add_department.html'
    success_url = reverse_lazy('department_list')
    permission_required = 'Department.change_dept_details'
    pk_url_kwarg = 'id'


# Delete Department (Admin Only - Delete Permission)
class DeleteDepartmentView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Dept_Details
    template_name = 'Department/confirm_delete.html'
    success_url = reverse_lazy('department_list')
    permission_required = 'Department.delete_dept_details'
    pk_url_kwarg = 'id'
























# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required, permission_required
# from .models import Dept_Details
# from .forms import DeptForm
#
#
# # View Departments (Login Required)
# @login_required
# def department_list(request):
#     departments = Dept_Details.objects.all()
#     return render(request, 'department_list.html', {'departments': departments})
#
#
# # Add Department (Only Admin Group - has add permission)
# @login_required
# @permission_required('Department.add_dept_details', raise_exception=True)
# def add_department(request):
#     if request.method == 'POST':
#         form = DeptForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('department_list')
#     else:
#         form = DeptForm()
#
#     return render(request, 'add_department.html', {'form': form})
#
#
# # Edit Department (Staff + Admin - change permission)
# @login_required
# @permission_required('Department.change_dept_details', raise_exception=True)
# def edit_department(request, id):
#     department = get_object_or_404(Dept_Details, dept_id=id)
#
#     if request.method == 'POST':
#         form = DeptForm(request.POST, instance=department)
#         if form.is_valid():
#             form.save()
#             return redirect('department_list')
#     else:
#         form = DeptForm(instance=department)
#
#     return render(request, 'add_department.html', {'form': form})
#
#
# # Delete Department (Admin Only - delete permission)
# @login_required
# @permission_required('Department.delete_dept_details', raise_exception=True)
# def delete_department(request, id):
#     department = get_object_or_404(Dept_Details, dept_id=id)
#     department.delete()
#     return redirect('department_list')

















# from .forms import DeptForm
# from django.shortcuts import redirect
# from django.shortcuts import render
# from .models import Dept_Details
#
# # Create your views here.
#
# def department_list(request):
#     departments = Dept_Details.objects.all()
#     return render(request, 'department_list.html', {'departments': departments})
#
# def add_department(request):
#     if request.method == 'POST':
#         form = DeptForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('department_list')
#     else:
#         form = DeptForm()
#
#     return render(request, 'add_department.html', {'form': form})
#
#
#
# def edit_department(request, id):
#     department = Dept_Details.objects.get(dept_id=id)
#
#     if request.method == 'POST':
#         form = DeptForm(request.POST, instance=department)
#         if form.is_valid():
#             form.save()
#             return redirect('department_list')
#     else:
#         form = DeptForm(instance=department)
#
#     return render(request, 'add_department.html', {'form': form})
#
#
# def delete_department(request, id):
#     department = Dept_Details.objects.get(dept_id=id)
#     department.delete()
#     return redirect('department_list')