from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Tag(models.Model):
    label = models.CharField(max_length=255, verbose_name='عنوان برچسب')

    class Meta:
        verbose_name = 'برچسبی'
        verbose_name_plural = ' برچسب ها'
        ordering = ['label']


class TagItem(models.Model):
    tag = models.ForeignKey(
        'Tag', on_delete=models.CASCADE, verbose_name='برچسب')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = 'برچسب های انتخابی'
        verbose_name_plural = 'برچسب انتخابی توسط کاربر'
