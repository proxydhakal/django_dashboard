from django.db import models
from django.urls import reverse
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=60, unique=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("design", kwargs={"name": self.name})
   