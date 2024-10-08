# Generated by Django 5.1.1 on 2024-09-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
