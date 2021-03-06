# Generated by Django 3.2.10 on 2021-12-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='artist',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='born',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='died',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='period',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='artist',
            name='profession',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='artist',
            name='region',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
