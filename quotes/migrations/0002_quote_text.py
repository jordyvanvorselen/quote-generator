# Generated by Django 2.0.7 on 2018-07-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='text',
            field=models.TextField(default='Goals transform a random walk into a chase.'),
            preserve_default=False,
        ),
    ]
