# Generated by Django 5.1.2 on 2024-10-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0005_alter_sfyj_hdsj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sfyj',
            name='hdsj',
            field=models.DateTimeField(blank=True, null=True, verbose_name='活动时间'),
        ),
    ]
