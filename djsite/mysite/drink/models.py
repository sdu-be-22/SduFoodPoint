from django.db import models


# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to="img/%y", null = True, blank=True, default='default.jpg')
    def __str__(self):
        return self.name