# Generated by Django 4.2 on 2023-08-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_alter_demande_adress_alter_demande_nomprenom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='a_prix',
            field=models.CharField(max_length=50),
        ),
    ]
