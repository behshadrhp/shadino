# Generated by Django 4.1.4 on 2023-01-04 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_cartitem_quantity_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['-created'], 'verbose_name': 'ادرسی', 'verbose_name_plural': 'ادرس مشتریان'},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['-created'], 'verbose_name': 'سبدی', 'verbose_name_plural': 'سبد ها'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'ordering': ['-created'], 'verbose_name': 'سبد خریدی', 'verbose_name_plural': 'سبد خرید ها'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['-created'], 'verbose_name': 'مجموعه ای', 'verbose_name_plural': 'مجموعه ها'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['birthday'], 'verbose_name': 'مشتری', 'verbose_name_plural': 'مشتریان'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-placed_at'], 'verbose_name': 'وضعیت سفارشی', 'verbose_name_plural': 'وضعیت سفارشات'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['-created'], 'verbose_name': 'سفارشی', 'verbose_name_plural': 'سفارشات'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-updated'], 'verbose_name': 'محصولی', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterModelOptions(
            name='promotion',
            options={'verbose_name': 'تبلیغی', 'verbose_name_plural': 'تبلیغات'},
        ),
    ]
