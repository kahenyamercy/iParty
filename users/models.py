from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    user_permissions = models.ManyToManyField(
        'auth.Permission', blank=True, related_name='custom_user_permissions')
    groups = models.ManyToManyField(
        'auth.Group', blank=True, related_name='custom_user_groups')

    objects = CustomUserManager()

    # Ensure to use this model as the custom user model
    class Meta:
        db_table = 'custom_user'

class Student(models.Model):
    campus = models.OneToOneField(
        'campus.Campus', on_delete=models.CASCADE)
    events = models.ManyToManyField(
        'events.Event', blank=True, related_name='user_events')
