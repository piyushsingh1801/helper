# Generated by Django 4.1.5 on 2023-03-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_profile_otp_remove_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
