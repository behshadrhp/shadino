from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from uuid import uuid4


# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    username_regex = RegexValidator(
        regex=r'^[a-zA-Z]{6,30}$', message='نام کاربری باید بین 6 تا 30 کاراکتر باشد و فقط حروف کوچک و بزرگ لاتین مجاز است')
    username = models.CharField(
        max_length=30, unique=True, verbose_name='نام کاربری', validators=[username_regex])
    first_name = models.CharField(max_length=25, verbose_name='نام')
    last_name = models.CharField(max_length=25, verbose_name='نام خانوادگی')
    email = models.EmailField(unique=True, verbose_name='ایمیل')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']