# Generated by Django 4.1.4 on 2023-01-05 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_promotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotion',
            field=models.ManyToManyField(blank=True, related_name='promotion_item', to='store.promotion', verbose_name='تبلیغات'),
        ),
    ]