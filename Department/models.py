from django.db import models

# Create your models here.
class Dept_Details(models.Model):
    dept_id=models.AutoField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    total_staff = models.IntegerField()
    total_student = models.IntegerField()

    def __str__(self):
        return self.dept_name