# Generated by Django 5.1.2 on 2024-11-22 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0052_backout_fz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backout',
            name='fz',
        ),
    ]
