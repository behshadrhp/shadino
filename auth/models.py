from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    first_name = models.CharField(max_length=25, verbose_name='نام')
    last_name = models.CharField(max_length=25, verbose_name='نام خانوادگی')
    username = models.CharField(
        max_length=25, unique=True, verbose_name='نام کاربری')
    email = models.EmailField(
        unique=True, max_length=254, verbose_name='ایمیل')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
