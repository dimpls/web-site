# Generated by Django 4.2.1 on 2023-05-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tattoos_made',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
