# Generated by Django 4.0.3 on 2022-03-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to='%Y/%m/%d/'),
        ),
    ]