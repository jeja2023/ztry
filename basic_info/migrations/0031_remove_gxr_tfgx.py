# Generated by Django 5.1.2 on 2024-11-06 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0030_alter_basicinfo_zt_alter_dtimage_cz_alter_jtimage_cz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gxr',
            name='tfgx',
        ),
    ]