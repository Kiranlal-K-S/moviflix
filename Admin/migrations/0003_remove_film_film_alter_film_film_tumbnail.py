# Generated by Django 5.0.3 on 2024-07-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_alter_film_film_alter_film_film_tumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='film',
        ),
        migrations.AlterField(
            model_name='film',
            name='film_tumbnail',
            field=models.ImageField(default='null.jpg', upload_to='film_tumbnail'),
        ),
    ]
