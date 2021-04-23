from django.db import models

from navigationbar.models import Navigation


# Create your models here.
class CategoryByNav(models.Model):
    title = models.CharField(max_length=20)
    link = models.TextField(max_length=100)
    product = models.ForeignKey(Navigation, on_delete=models.CASCADE)
