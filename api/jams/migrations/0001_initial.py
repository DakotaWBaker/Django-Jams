# Generated by Django 4.1.3 on 2022-11-15 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled', max_length=255)),
                ('duration', models.FloatField()),
                ('number_of_plays', models.IntegerField(default=0)),
            ],
        ),
    ]