# Generated by Django 4.2.1 on 2023-05-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_review_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='default_image.png', upload_to='user_photos'),
        ),
    ]
