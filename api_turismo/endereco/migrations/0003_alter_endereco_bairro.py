# Generated by Django 3.2.6 on 2021-08-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_auto_20210816_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.TextField(max_length=150),
        ),
    ]
