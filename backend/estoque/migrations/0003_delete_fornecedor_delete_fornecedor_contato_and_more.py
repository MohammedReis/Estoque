# Generated by Django 4.0.2 on 2022-02-28 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_rename_cnpj_fornecedor_cnpj_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fornecedor',
        ),
        migrations.DeleteModel(
            name='Fornecedor_Contato',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Solicitacao',
        ),
    ]
