# Generated by Django 5.1 on 2024-08-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_fornecedores', '0002_rename_fornecedores_fornecedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='celular',
            field=models.IntegerField(default='00000000000'),
            preserve_default=False,
        ),
    ]
