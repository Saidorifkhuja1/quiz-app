# Generated by Django 5.0.4 on 2024-05-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_is_teacher_customer_are_you_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='receive_newsletter',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='receive_notifications',
            field=models.BooleanField(default=True),
        ),
    ]
