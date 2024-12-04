# Generated by Django 5.1.2 on 2024-11-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0027_alter_basicinfo_id_card_alter_gxr_id_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='zt',
            field=models.CharField(choices=[('1', '在逃'), ('2', '撤销'), ('3', '已抓获未撤销')], default='1', max_length=50, verbose_name='状态'),
        ),
    ]
