# Generated by Django 5.1.4 on 2025-03-11 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_category_product_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Fournisseur',
                'verbose_name_plural': 'Fournisseurs',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produit', 'verbose_name_plural': 'Produits'},
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='myapp.supplier'),
        ),
    ]
