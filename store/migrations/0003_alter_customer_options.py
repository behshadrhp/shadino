# Generated by Django 4.1.6 on 2023-02-10 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_customer_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['birthday'], 'permissions': [('view_history', 'can view history')], 'verbose_name': 'مشتری', 'verbose_name_plural': 'مشتریان'},
        ),
    ]
