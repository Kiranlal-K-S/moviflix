# Generated by Django 5.0.3 on 2024-07-19 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_film_film_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='film',
            name='film_genres',
        ),
    ]
