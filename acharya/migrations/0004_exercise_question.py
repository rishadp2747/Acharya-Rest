# Generated by Django 3.0.8 on 2020-08-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acharya', '0003_auto_20200811_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='question',
            field=models.TextField(default=''),
        ),
    ]