# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 13:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0015_auto_20180112_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexNovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=10, verbose_name='推荐的小说标题')),
                ('novel_image', models.ImageField(blank=True, null=True, upload_to='tuiimg/%Y/%m', verbose_name='推荐小说的封面图')),
                ('addtime', models.DateField(default=datetime.datetime.now, verbose_name='推荐时间')),
            ],
            options={
                'verbose_name': '小说展示',
                'verbose_name_plural': '小说展示',
                'db_table': 'IndexNovel',
            },
        ),
        migrations.AddField(
            model_name='novelmodel',
            name='novel_Recommend',
            field=models.BooleanField(default=False, verbose_name='是否幻灯片推荐'),
        ),
        migrations.AddField(
            model_name='indexnovel',
            name='novel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel.NovelModel', verbose_name='推荐的小说'),
        ),
    ]
