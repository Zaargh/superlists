# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
