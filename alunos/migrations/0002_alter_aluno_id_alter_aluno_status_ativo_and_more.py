# Generated by Django 4.0.4 on 2022-04-16 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='id',
            field=models.PositiveBigIntegerField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='status_ativo',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='status_pendencia',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
