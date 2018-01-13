# Generated by Django 2.0 on 2018-01-13 03:15

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', accounts.models.EmailLoginField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Last Name')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is admin?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff?')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]