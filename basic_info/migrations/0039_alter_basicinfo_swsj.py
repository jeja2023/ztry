# Generated by Django 5.1.2 on 2024-11-18 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0038_basicinfo_jyaq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='swsj',
            field=models.DateTimeField(blank=True, null=True, verbose_name='上网时间'),
        ),
    ]
