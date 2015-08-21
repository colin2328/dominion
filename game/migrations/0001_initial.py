# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turn_count', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('race_choice', models.SmallIntegerField(default=1, choices=[(1, b'Human'), (2, b'Elf')])),
                ('num_population', models.IntegerField(default=250, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_mana', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_units', models.IntegerField(default=200, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_acres', models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_lumber', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_gold', models.IntegerField(default=10000, validators=[django.core.validators.MinValueValidator(0)])),
                ('game', models.ForeignKey(to='game.Game')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
