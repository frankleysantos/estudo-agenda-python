# Generated by Django 4.0.4 on 2022-06-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
