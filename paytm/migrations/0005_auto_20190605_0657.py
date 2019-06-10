# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0004_auto_20190605_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNID',
            field=models.CharField(verbose_name='TXN ID', max_length=200),
        ),
    ]
