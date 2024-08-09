import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models

from .managers import CustomUserManager

from apps.core.models import UUIDModel


# Create your models here.
class Employee(AbstractBaseUser, UUIDModel, PermissionsMixin):
    EMPLOYEE = "employee"
    LINE_MANAGER = "line_manager"
    ORGANIZATION_ADMIN = "admin"
    USER_TYPE_CHOICES = (
        (EMPLOYEE, "Employee"),
        (LINE_MANAGER, "Line Manager"),
        (ORGANIZATION_ADMIN, "Organization Admin"),
    )
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    user_type = models.CharField(
        max_length=255, choices=USER_TYPE_CHOICES, default=EMPLOYEE
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
