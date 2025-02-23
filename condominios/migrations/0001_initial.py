# Generated by Django 5.1.6 on 2025-02-14 00:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_custom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo do condomínio.', max_length=100, verbose_name='Nome do Condomínio')),
                ('endereco', models.CharField(help_text='Endereço completo do condomínio.', max_length=200, verbose_name='Endereço')),
                ('provincia', models.CharField(blank=True, choices=[('Bengo', 'Bengo'), ('Cuanza-Norte', 'Cuanza-Norte'), ('Cuanza-Sul', 'Cuanza-Sul'), ('Huambo', 'Huambo'), ('Bié', 'Bié'), ('Moxico', 'Moxico'), ('Moxico-Leste', 'Moxico-Leste'), ('Lunda-Norte', 'Lunda-Norte'), ('Lunda-Sul', 'Lunda-Sul'), ('Ecolo e Bengo', 'Ecolo e Bengo'), ('Huíla', 'Huíla'), ('Cunene', 'Cunene'), ('Cabinda', 'Cabinda'), ('Zaire', 'Zaire'), ('Uíge', 'Uíge'), ('Malanje', 'Malanje'), ('Cuando', 'Cuando'), ('Cubango', 'Cubango'), ('Luanda', 'Luanda')], default='Luanda', help_text='Província onde o condomínio está localizado (apenas para Angola).', max_length=50, null=True, verbose_name='Província')),
                ('estado', models.CharField(blank=True, help_text='Estado ou província onde o condomínio está localizado (para países fora de Angola).', max_length=100, null=True, verbose_name='Estado/Província')),
                ('nif', models.CharField(blank=True, help_text='Número de Identificação Fiscal do condomínio.', max_length=20, null=True, verbose_name='NIF')),
                ('pais', models.CharField(choices=[('Angola', 'Angola'), ('Brasil', 'Brasil'), ('Cabo Verde', 'Cabo Verde'), ('Guiné-Bissau', 'Guiné-Bissau'), ('Guiné Equatorial', 'Guiné Equatorial'), ('Moçambique', 'Moçambique'), ('Portugal', 'Portugal'), ('São Tomé e Príncipe', 'São Tomé e Príncipe'), ('Timor-Leste', 'Timor-Leste')], default='Angola', help_text='País onde o condomínio está localizado.', max_length=50, verbose_name='País')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, help_text='Data e hora em que o condomínio foi cadastrado.', verbose_name='Data de Cadastro')),
                ('tipo_condominio', models.CharField(choices=[('predio', 'Prédio'), ('vivenda', 'Vivenda')], default='predio', help_text='Tipo de condomínio (Prédio ou Vivenda).', max_length=10, verbose_name='Tipo de Condomínio')),
                ('numero_andares', models.IntegerField(blank=True, help_text='Número total de andares do condomínio (apenas para prédios).', null=True, verbose_name='Número de Andares')),
                ('numero_apartamentos', models.IntegerField(blank=True, help_text='Número total de apartamentos no condomínio (apenas para prédios).', null=True, verbose_name='Número de Apartamentos')),
                ('numero_vivendas', models.IntegerField(blank=True, help_text='Número total de vivendas no condomínio (apenas para condomínios de vivendas).', null=True, verbose_name='Número de Vivendas')),
                ('logo', models.ImageField(blank=True, help_text='Logo do condomínio.', null=True, upload_to='condominios/logos/', verbose_name='Logo')),
                ('proprietario', models.ForeignKey(help_text='Proprietário responsável pelo condomínio.', on_delete=django.db.models.deletion.CASCADE, related_name='condominios', to='auth_custom.user', verbose_name='Proprietário')),
            ],
            options={
                'verbose_name': 'Condomínio',
                'verbose_name_plural': 'Condomínios',
            },
        ),
    ]
