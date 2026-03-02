from .forms import DeptForm
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Dept_Details

# Create your views here.

def department_list(request):
    departments = Dept_Details.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def add_department(request):
    if request.method == 'POST':
        form = DeptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DeptForm()

    return render(request, 'add_department.html', {'form': form})



def edit_department(request, id):
    department = Dept_Details.objects.get(dept_id=id)

    if request.method == 'POST':
        form = DeptForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DeptForm(instance=department)

    return render(request, 'add_department.html', {'form': form})


def delete_department(request, id):
    department = Dept_Details.objects.get(dept_id=id)
    department.delete()
    return redirect('department_list')