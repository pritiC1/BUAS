from django.db import models
from django.contrib.auth.models import AbstractUser
import random

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    email = models.EmailField(unique=True)  # Remove null=True
    contact_number = models.CharField(max_length=15, null=True)
    date_of_birth= models.DateField(null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)  # Field for storing OTP
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)  # 6-digit OTP
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'contact_number']

    def __str__(self):
        return self.email
    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.save()
