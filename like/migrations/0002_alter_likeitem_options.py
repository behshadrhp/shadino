# Generated by Django 4.1.4 on 2023-01-04 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likeitem',
            options={'verbose_name': 'پسندیده شده ها', 'verbose_name_plural': 'پسندیده شده توسط کاربر'},
        ),
    ]