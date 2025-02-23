# Generated by Django 5.1.6 on 2025-02-14 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_custom', '0002_rename_cpf_user_nif'),
        ('condominios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTransacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Transação')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data da Despesa')),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoria')),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='despesas', to='condominios.condominio')),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data da Transação')),
                ('comprovativo', models.FileField(blank=True, null=True, upload_to='comprovativos/', verbose_name='Comprovativo')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacoes', to='condominios.condominio')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacoes', to='financeiro.tipotransacao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacoes', to='auth_custom.user')),
            ],
        ),
    ]
