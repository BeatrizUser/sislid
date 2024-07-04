# Generated by Django 3.2 on 2024-07-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20240527_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cep',
            field=models.CharField(default='000', max_length=10),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_de_nascimento',
            field=models.DateField(blank=True, help_text='Exemplo: 01/01/1990', null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='observacao',
            field=models.TextField(blank=True, null=True, verbose_name='Histórico'),
        ),
    ]