# Generated by Django 3.1.6 on 2021-02-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuetodoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]