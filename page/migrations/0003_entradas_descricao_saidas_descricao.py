# Generated by Django 4.2 on 2023-04-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_categoria_usuario_entradas_usuario_saidas_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradas',
            name='descricao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='saidas',
            name='descricao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição'),
        ),
    ]