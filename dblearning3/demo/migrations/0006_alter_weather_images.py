# Generated by Django 5.0.1 on 2024-02-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_alter_weather_image_path_alter_weather_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='images',
            field=models.FileField(null=True, upload_to='static/uploads/'),
        ),
    ]