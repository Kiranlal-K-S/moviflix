# Generated by Django 5.0.3 on 2024-07-24 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_reg_u_address_user_reg_u_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_reg',
            name='u_name',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
