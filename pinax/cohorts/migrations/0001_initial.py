# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 21:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_fix_str'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='name')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
            ],
            options={
                'permissions': (('manage_cohorts', 'Can manage cohorts'),),
            },
        ),
        migrations.CreateModel(
            name='SignupCodeCohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_cohorts.Cohort')),
                ('signup_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.SignupCode')),
            ],
        ),
        migrations.CreateModel(
            name='UserCohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_cohorts.Cohort')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
