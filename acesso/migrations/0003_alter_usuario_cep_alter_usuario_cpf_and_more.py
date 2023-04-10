# Generated by Django 4.2 on 2023-04-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0002_usuario_first_name_usuario_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cep',
            field=models.CharField(max_length=15, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Admin'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=30, unique=True, verbose_name='Usuário'),
        ),
    ]
