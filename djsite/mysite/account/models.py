from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length= 50, unique=True)
    first_name = models.CharField(max_length= 50, unique=True)
    last_name = models.CharField(max_length= 50, unique=True)
    email = models.EmailField(verbose_name='email address', blank=True, max_length=60, unique=True)
    birthdate = models.DateField(verbose_name='birthday')
    have_allergies = models.BooleanField(default=True)
    phone_number = PhoneNumberField()
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(default=True)