from django.db import models


# Create your models here.
class Eat(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=255, default='')
    price = models.IntegerField(null=True, blank = True)
    image = models.ImageField(upload_to="img/%y", null = True, blank=True, default='default.jpg')
    def __str__(self):
        return self.name