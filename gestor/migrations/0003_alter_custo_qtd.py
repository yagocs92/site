# Generated by Django 4.2.2 on 2023-06-19 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0002_alter_custo_preco_unit_alter_custo_qtd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custo',
            name='qtd',
            field=models.IntegerField(),
        ),
    ]
