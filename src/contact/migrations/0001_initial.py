# Generated by Django 2.0 on 2018-04-05 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name')),
                ('credential', models.CharField(blank=True, choices=[('A', 'Athlete'), ('T', 'Team'), ('L', 'League Organizer'), ('O', 'Other')], max_length=200, null=True, verbose_name='Credential')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email Address')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('datesent', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
    ]