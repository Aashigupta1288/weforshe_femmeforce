# Generated by Django 2.2.8 on 2023-08-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
