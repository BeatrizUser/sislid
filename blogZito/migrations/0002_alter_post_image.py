# Generated by Django 3.2 on 2024-05-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogZito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='post_images/'),
            preserve_default=False,
        ),
    ]