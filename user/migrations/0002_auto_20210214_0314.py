# Generated by Django 3.1.6 on 2021-02-14 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password_1',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password_2',
            new_name='password2',
        ),
    ]
