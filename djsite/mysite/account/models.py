from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True) # 1-*
    birthdate = models.DateField(verbose_name='birthday')
    have_allergies = models.BooleanField(default=False)
    phone_number = PhoneNumberField()
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="img/%y", null = True, blank=True, default='blank.png')

    def __str__(self):
        return self.user.__str__()