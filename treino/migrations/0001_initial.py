# Generated by Django 5.1.6 on 2025-02-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('faixa', models.CharField(choices=[('B', 'Branca'), ('Y', 'Amarela'), ('G', 'Verde'), ('A', 'Azul'), ('R', 'Roxa'), ('M', 'Marrom'), ('P', 'Preta'), ('V', 'Vermelha')], default='B', max_length=1)),
            ],
        ),
    ]
