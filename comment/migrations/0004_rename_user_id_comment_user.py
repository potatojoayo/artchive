# Generated by Django 3.2.10 on 2021-12-15 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20211210_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
    ]
