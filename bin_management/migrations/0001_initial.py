# Generated by Django 5.0.7 on 2024-09-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_id', models.CharField(max_length=10, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('weight', models.FloatField(default=0.0)),
                ('trash_level', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
