# Generated by Django 5.0.3 on 2024-03-27 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_similar_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name': 'ProductImage', 'verbose_name_plural': 'ProductImages'},
        ),
        migrations.AlterModelTable(
            name='productimages',
            table=None,
        ),
    ]
