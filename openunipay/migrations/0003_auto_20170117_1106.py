# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openunipay', '0002_remove_alipayorder_interface_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weixinorder',
            name='total_fee',
            field=models.PositiveIntegerField(editable=False, verbose_name='总金额'),
        ),
    ]