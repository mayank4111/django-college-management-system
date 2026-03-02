from django import forms
from .models import Dept_Details

class DeptForm(forms.ModelForm):
    class Meta:
        model = Dept_Details
        fields = ['dept_name', 'hod', 'total_staff', 'total_student']