# Generated by Django 4.2 on 2023-05-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]