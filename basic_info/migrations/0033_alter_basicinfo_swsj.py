# Generated by Django 5.1.2 on 2024-11-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0032_alter_basicinfo_ztrybh_alter_dtimage_ztrybh_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='swsj',
            field=models.DateTimeField(blank=True, null=True, verbose_name='上网时间'),
        ),
    ]