# Generated by Django 5.0.3 on 2024-07-25 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_watch_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch_list',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
