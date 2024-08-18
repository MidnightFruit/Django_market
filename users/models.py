from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True, verbose_name='Почта', null=False, blank=False)
    avatar = models.ImageField(verbose_name='Аватарка', null=True, blank=True)
    phone_number = models.CharField(max_length=11, verbose_name='Телефонный номер', unique=True)
    country = models.CharField(max_length=26, verbose_name="Страна")

    token = models.CharField(max_length=255, verbose_name="Токен", blank=True, null=True)

    REQUIRED_FIELDS = []
