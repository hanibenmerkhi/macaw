# Generated by Django 4.2 on 2023-08-11 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0009_delete_demande_delete_produit'),
    ]

    operations = [
        migrations.CreateModel(
            name='demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomprenom', models.CharField(blank=True, max_length=500)),
                ('num', models.IntegerField(blank=True)),
                ('adress', models.TextField(blank=True)),
                ('pro', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name': 'demande',
            },
        ),
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('desc', models.TextField()),
                ('prix', models.IntegerField()),
                ('a_prix', models.IntegerField(blank=True, null=True)),
                ('promo', models.BooleanField(default=False)),
                ('pack', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='photos')),
            ],
            options={
                'verbose_name': 'produit',
            },
        ),
    ]