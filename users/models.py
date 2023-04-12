from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = 'Пользователь'
    ADMIN = 'Администратор'
    ROLE = [(USER, 'user'), (ADMIN, 'admin')]


class User(AbstractUser):
    email = models.EmailField(_('email'), db_index=True, max_length=60, unique=True, blank=True)
    phone = models.CharField(_('phone'), max_length=12, null=False, blank=False)
    role = models.CharField(_('role'), max_length=15, choices=UserRoles.ROLE, default=UserRoles.USER)
    last_login = models.DateTimeField(_('last_login'), auto_now=True)
    image = models.ImageField(_('image'), upload_to="img_users")

    def image_(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="150"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_.short_description = 'Аватарка пользователя'
    image_.allow_tags = True

    # Необходимые параметры для корректной работе Django
    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # В качестве подсказки — эти поля имеют
    # непосредственное отношение именно к нашей модели
    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя
    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN  #

    @property
    def is_user(self):
        return self.role == UserRoles.USER
