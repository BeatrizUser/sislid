# Generated by Django 3.2.24 on 2024-02-24 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20240224_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='endereco',
            new_name='rua',
        ),
        migrations.RenameField(
            model_name='pessoa',
            old_name='genero',
            new_name='sexo',
        ),
    ]