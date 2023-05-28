# Generated by Django 4.2.1 on 2023-05-28 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_planner', '0005_meeting_day_meeting_end_date_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFreeTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Начало свободного времени')),
                ('end_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Конец свободного времени')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
