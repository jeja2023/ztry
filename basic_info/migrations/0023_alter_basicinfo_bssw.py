# Generated by Django 5.1.2 on 2024-11-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0022_remove_ypjl_xq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='bssw',
            field=models.TextField(blank=True, default='否', max_length=50, null=True, verbose_name='本市上网'),
        ),
    ]
