# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trim_id', models.IntegerField()),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=32)),
                ('model', models.CharField(max_length=16)),
                ('trim_name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VSNPattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pattern', models.CharField(max_length=16)),
                ('vehicle', models.ForeignKey(to='vehicles.Vehicle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
