# Generated by Django 5.1.2 on 2024-11-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0055_rename_zgdw_zhzg_zhdw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhzg',
            name='zhdw',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='抓获单位'),
        ),
    ]
