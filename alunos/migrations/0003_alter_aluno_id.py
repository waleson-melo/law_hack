# Generated by Django 4.0.4 on 2022-04-16 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_alter_aluno_id_alter_aluno_status_ativo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
