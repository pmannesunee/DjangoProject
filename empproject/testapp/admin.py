from django.contrib import admin
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal']
# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
