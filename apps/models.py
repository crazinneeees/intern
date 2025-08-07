from django.db import models
from django.db.models import Model, CharField, TextField, ForeignKey, DateTimeField, EmailField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have email')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Event(Model):
    title = CharField(max_length=100)
    description = TextField()
    date = DateTimeField(auto_now_add=True)
    location = CharField(max_length=100)
    organizer = ForeignKey('apps.CustomUser', related_name='organizers', on_delete = models.CASCADE)


class Registration(Model):
    user = ForeignKey('apps.CustomUser', on_delete = models.CASCADE)
    event = ForeignKey('apps.Event', on_delete = models.CASCADE)
    registered_at = DateTimeField(auto_now_add=True)
