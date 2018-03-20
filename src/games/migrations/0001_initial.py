# Generated by Django 2.0 on 2018-03-20 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='teams.Team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='leagues.League')),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
                ('user_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SoccerGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
            ],
        ),
    ]
