# Generated by Django 5.1.2 on 2024-11-15 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0034_basicinfo_xxzjbh'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gz',
            unique_together={('ztrybh', 'gzr')},
        ),
    ]
