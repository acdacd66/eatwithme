from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    code = models.IntegerField(null = True)
    department = models.CharField(max_length=200, null= True)
   