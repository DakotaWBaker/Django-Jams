# Generated by Django 4.1.3 on 2022-11-16 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0007_alter_song_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='about',
            field=models.CharField(default='Untitled', max_length=1000),
        ),
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='jams.genre'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(blank=True, to='jams.artist'),
        ),
    ]