from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


class Command(BaseCommand):
    help = "Create a superuser with email and password"

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        Employee = get_user_model()
        email = settings.SUPERUSER_EMAIL
        password = settings.SUPERUSER_PASSWORD

        if not Employee.objects.filter(email=email).exists():
            Employee.objects.create_superuser(email=email, password=password)
            self.stdout.write(
                self.style.SUCCESS(f"Superuser created with email: {email}")
            )
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))
