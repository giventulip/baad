from django.db import models

# Create your models here.
class Navigation(models.Model):
    title = models.CharField(max_length=20)
    link = models.TextField(max_length=100)
    icon = models.CharField(max_length=20, default="fa-")
    on_categorys = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.title