from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class BankUser(AbstractUser):
    bank_number = models.CharField(max_length=256, blank=True, null=True)
    money = models.CharField(max_length=256, blank=True, null=True)
