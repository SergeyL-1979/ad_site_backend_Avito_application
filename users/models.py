from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserRoles(models.Model):
    # TODO закончите enum-класс для пользователя
    name_user = models.CharField(max_length=100)
    phone = PhoneNumberField(null=False, blank=False, unique=True)


# class User(AbstractBaseUser):
#     # TODO переопределение пользователя.
#     # TODO подробности также можно поискать в рекоммендациях к проекту
#     pass
