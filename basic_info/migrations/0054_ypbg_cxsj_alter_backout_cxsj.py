# Generated by Django 5.1.2 on 2024-11-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0053_remove_backout_fz'),
    ]

    operations = [
        migrations.AddField(
            model_name='ypbg',
            name='cxsj',
            field=models.DateTimeField(blank=True, null=True, verbose_name='撤销时间'),
        ),
        migrations.AlterField(
            model_name='backout',
            name='cxsj',
            field=models.DateTimeField(blank=True, null=True, verbose_name='撤销时间'),
        ),
    ]
