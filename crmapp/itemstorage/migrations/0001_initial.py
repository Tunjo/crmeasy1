# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemStorage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('disc', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('choice', models.PositiveSmallIntegerField(choices=[(1, b'Books'), (2, b'Beverage'), (3, b'Games')])),
            ],
            options={
                'verbose_name_plural': 'itemstorages',
            },
            bases=(models.Model,),
        ),
    ]
