# Generated by Django 5.2 on 2025-04-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='manually_added',
            field=models.BooleanField(default=False),
        ),
    ]
