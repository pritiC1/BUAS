# Generated by Django 5.1.1 on 2024-09-25 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_delete_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
