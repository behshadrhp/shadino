# Generated by Django 4.1.4 on 2023-01-17 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'ordering': ['-created'], 'verbose_name': 'سبد خریدی', 'verbose_name_plural': 'سبد خرید'},
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_item', to='store.product', verbose_name='محصول'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]