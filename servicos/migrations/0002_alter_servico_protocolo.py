# Generated by Django 4.1.1 on 2022-10-14 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='protocolo',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
    ]
