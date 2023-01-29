from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from auth.models import User

# Create your models here.

class LikeItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = 'پسندیده شده ها'
        verbose_name_plural = 'پسندیده شده توسط کاربر'