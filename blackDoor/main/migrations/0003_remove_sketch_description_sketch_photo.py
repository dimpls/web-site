# Generated by Django 4.2.1 on 2023-05-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_date_of_birth_user_tattoos_made'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sketch',
            name='description',
        ),
        migrations.AddField(
            model_name='sketch',
            name='photo',
            field=models.ImageField(default='default_image.png', upload_to='sketch_photos'),
        ),
    ]
