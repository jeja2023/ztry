# Generated by Django 5.1.2 on 2024-10-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0006_alter_sfyj_hdsj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gxr',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ztrybh', models.CharField(max_length=50, verbose_name='在逃人员编号')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='姓名')),
                ('id_card', models.CharField(blank=True, max_length=18, null=True, verbose_name='身份证号码')),
                ('gxr_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='关系人姓名')),
                ('gxr_id', models.DateTimeField(blank=True, max_length=18, null=True, verbose_name='关系人身份证号码')),
                ('hzgx', models.CharField(blank=True, max_length=50, null=True, verbose_name='关系人与户主关系')),
                ('tfgx', models.CharField(blank=True, max_length=100, null=True, verbose_name='关系人与逃犯关系')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '在逃关系人',
                'verbose_name_plural': '在逃关系人',
            },
        ),
    ]