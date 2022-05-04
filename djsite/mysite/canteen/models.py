from django.db import models
from account.models import Account
from drink.models import Drink
from eat.models import Eat


class SalesOrder(models.Model):
    description = models.CharField(max_length=255)
    amount = models.IntegerField()
    food = models.ManyToManyField(Eat) # *-*
    drink = models.ManyToManyField(Drink) # *-*
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)  # 1-1
    def __str__(self):
        return self.account


class Comment(models.Model):
    photo = models.ImageField(upload_to="img/%y", null = True, blank=True, default='default.jpg')
    user = models.CharField(max_length=30)
    comment = models.TextField(max_length=255)
    def __str__(self):
        return self.user
