# Generated by Django 5.0.3 on 2024-05-21 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(blank=True, default='', help_text='This is for name', max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='order',
            field=models.IntegerField(default=0, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='percentage',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percantage'),
        ),
    ]
