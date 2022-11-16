# Generated by Django 4.1.3 on 2022-11-16 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0008_alter_artist_about_alter_artist_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jams.genre'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jams.genre'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='song_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jams.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(blank=True, null=True, to='jams.artist'),
        ),
    ]
