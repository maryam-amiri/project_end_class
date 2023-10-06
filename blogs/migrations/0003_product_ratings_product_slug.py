# Generated by Django 4.2.5 on 2023-09-22 07:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_product_description_alter_product_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ratings',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='امتیاز'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', verbose_name='عنوان در url'),
        ),
    ]
