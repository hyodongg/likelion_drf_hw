# Generated by Django 5.2.3 on 2025-07-15 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_rename_titme_song_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='singer',
            name='tags',
            field=models.ManyToManyField(blank=True, to='music.tag'),
        ),
    ]
