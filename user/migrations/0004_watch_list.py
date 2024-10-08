# Generated by Django 5.0.3 on 2024-07-24 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_film_genre_id'),
        ('user', '0003_user_reg_u_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watch_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('film_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.film')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user_reg')),
            ],
        ),
    ]
