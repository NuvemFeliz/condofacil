# Generated by Django 5.1.6 on 2025-02-14 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('condominios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Plano')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('preco_mensal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço Mensal')),
                ('limite_moradores', models.IntegerField(default=0, verbose_name='Limite de Moradores')),
                ('limite_funcionarios', models.IntegerField(default=0, verbose_name='Limite de Funcionários')),
                ('limite_espacos_comuns', models.IntegerField(default=0, verbose_name='Limite de Espaços Comuns')),
                ('suporte_prioritario', models.BooleanField(default=False, verbose_name='Suporte Prioritário')),
                ('relatorios_avancados', models.BooleanField(default=False, verbose_name='Relatórios Avançados')),
            ],
            options={
                'verbose_name': 'Plano',
                'verbose_name_plural': 'Planos',
            },
        ),
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('data_renovacao', models.DateField(blank=True, null=True, verbose_name='Data de Renovação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('condominio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='assinatura', to='condominios.condominio')),
                ('plano', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assinaturas', to='planos.plano')),
            ],
            options={
                'verbose_name': 'Assinatura',
                'verbose_name_plural': 'Assinaturas',
            },
        ),
    ]
