from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensures email is unique for authentication
    username = models.CharField(max_length=150, blank=True, null=True, unique=False)  # Set blank and null
    
    USERNAME_FIELD = 'email'  # Use email as the primary identifier for authentication
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Fields required when creating a superuser

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


