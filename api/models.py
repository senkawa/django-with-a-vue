from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


# TODO: https://stackoverflow.com/a/31093016


class User(AbstractUser):
    pass


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
