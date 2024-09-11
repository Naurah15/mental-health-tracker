# Generated by Django 5.1 on 2024-09-11 07:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoodEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mood', models.CharField(max_length=255)),
                ('time', models.DateField(auto_now_add=True)),
                ('feelings', models.TextField()),
                ('mood_intensity', models.IntegerField()),
            ],
        ),
    ]
