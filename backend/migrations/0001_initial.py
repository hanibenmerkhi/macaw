# Generated by Django 4.2 on 2023-08-08 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomprenom', models.CharField(max_length=500)),
                ('num', models.IntegerField()),
                ('adress', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom2', models.CharField(max_length=500)),
                ('desc2', models.TextField()),
                ('prix2', models.IntegerField()),
                ('a_prix2', models.IntegerField()),
                ('image2', models.ImageField(upload_to='photos/%y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom1', models.CharField(max_length=500)),
                ('desc1', models.TextField()),
                ('prix1', models.IntegerField()),
                ('a_prix1', models.IntegerField()),
                ('image1', models.ImageField(upload_to='photos/%y/%m/%d')),
            ],
        ),
    ]
