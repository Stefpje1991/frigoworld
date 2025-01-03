# Generated by Django 5.1.4 on 2024-12-24 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=100)),
                ('beschrijving', models.TextField(blank=True, null=True)),
                ('prijs', models.DecimalField(decimal_places=2, max_digits=10)),
                ('beschikbaar', models.BooleanField(default=True)),
                ('inhoud', models.CharField(blank=True, max_length=100, null=True)),
                ('categorie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='items.itemcategorie')),
            ],
        ),
    ]
