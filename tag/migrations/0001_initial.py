# Generated by Django 4.1.4 on 2023-01-30 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, verbose_name='عنوان برچسب')),
            ],
            options={
                'verbose_name': 'برچسبی',
                'verbose_name_plural': ' برچسب ها',
                'ordering': ['label'],
            },
        ),
        migrations.CreateModel(
            name='TagItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.UUIDField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.tag', verbose_name='برچسب')),
            ],
            options={
                'verbose_name': 'برچسب های انتخابی',
                'verbose_name_plural': 'برچسب انتخابی توسط کاربر',
            },
        ),
    ]
