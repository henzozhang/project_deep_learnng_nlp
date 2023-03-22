from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    name = models.fields.CharField(max_length=100)
    age = models.fields.IntegerField()
    email = models.fields.EmailField()
    mdp = models.fields.CharField(max_length=100)

    def __str__(self):
        return self.name

class ApiModel(models.Model):
    url = models.URLField(
        max_length=100,
        blank=False,
        null=True,
    )