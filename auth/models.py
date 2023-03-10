from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from validate_email_address import validate_email
from uuid import uuid4
from json import load


# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    username_regex = RegexValidator(
        regex=r'^[a-zA-Z]{6,30}$', message='نام کاربری باید بین 6 تا 30 کاراکتر باشد و فقط حروف کوچک و بزرگ لاتین مجاز است'
    )
    name_regex = RegexValidator(
        regex=r'^[\u0600-\u06FF\s]+$', message='فقط حروف فارسی مجاز است'
    )
    username = models.CharField(
        max_length=30, unique=True, verbose_name='نام کاربری', validators=[username_regex])
    first_name = models.CharField(
        max_length=25, verbose_name='نام', validators=[name_regex])
    last_name = models.CharField(
        max_length=25, verbose_name='نام خانوادگی', validators=[name_regex])
    email = models.EmailField(unique=True, verbose_name='ایمیل')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def clean(self):
        username = self.username
        username_lower = username.lower()
        email = self.email
        email_validation = validate_email(
            email=email, verify=True, check_mx=True)

        with open('auth/reserved-username/username.json', 'r') as username:
            reserved_username = load(username)

        for item in reserved_username:
            if username_lower == item:
                raise ValidationError(
                    'با عرض پوزش امکان استفاده از این نام کاربری امکان پذیر نمی باشد')

        if email_validation == False or email_validation == None:
            raise ValidationError(
                'ایمیل وارد شده معتبر نیست لطفا از یک ایمیل معتبر استفاده کنید')
