# Generated by Django 4.2 on 2023-08-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_alter_produit_a_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='pro',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produit',
            name='a_prix',
            field=models.CharField(max_length=50),
        ),
    ]