# Generated by Django 4.0.2 on 2022-03-03 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_aluno_data_fim_pagamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='data_fim_pagamento',
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], default='M', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.curso')),
            ],
        ),
    ]