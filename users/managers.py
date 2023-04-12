from django.contrib.auth.models import BaseUserManager


# здесь должен быть менеджер для модели Юзера.
# Поищите эту информацию в рекомендациях к проекту
# Менеджер должен содержать как минимум две следующие функции
class UserManager(BaseUserManager):
    """
    Функция создания пользователя — в нее мы передаем обязательные поля
    """

    def create_user(self, email, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role="user"
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, role=None, password=None):
        """
        Функция для создания суперпользователя — с ее помощью мы создаем администратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role
        )
        user.is_active = True
        # user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user
