# Generated by Django 4.1 on 2022-11-03 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0009_alter_inputmodel_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inputmodel',
            old_name='user_id',
            new_name='user',
        ),
    ]
