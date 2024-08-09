from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Employee

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "user_type"]
