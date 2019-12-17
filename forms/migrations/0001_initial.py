# Generated by Django 3.0 on 2019-12-17 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField(default=0)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('contado_responsavel', models.IntegerField(default=0)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('escolaridade', models.CharField(max_length=255)),
                ('profissao', models.CharField(max_length=255)),
                ('religiao', models.CharField(max_length=255)),
                ('orientacao_sexual', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sessoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_sessao', models.DateField(blank=True, null=True)),
                ('objetivos', models.CharField(max_length=255)),
                ('antecedente', models.CharField(max_length=255)),
                ('comportamento', models.CharField(max_length=255)),
                ('consequente', models.CharField(max_length=255)),
                ('intervencoes', models.CharField(max_length=255)),
                ('recursos', models.CharField(max_length=255)),
            ],
        ),
    ]