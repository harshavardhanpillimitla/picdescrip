# Generated by Django 3.0.2 on 2020-02-03 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='NULL', upload_to='posts_img'),
        ),
    ]