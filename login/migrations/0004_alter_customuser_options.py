# Generated by Django 5.1.2 on 2024-10-21 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
    ]