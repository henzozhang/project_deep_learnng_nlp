# Generated by Django 4.1 on 2022-10-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputmodel',
            name='text_msg',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]