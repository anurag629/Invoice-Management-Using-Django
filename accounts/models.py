from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    buissness_name = models.CharField(max_length=100)
    buissness_logo = models.ImageField(upload_to='logo')
    address_line1 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField(null=True)

    objects = UserManager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
