# Generated by Django 2.0 on 2019-07-17 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_signup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup',
            new_name='register',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='name',
            new_name='username',
        ),
    ]
