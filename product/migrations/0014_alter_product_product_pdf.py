# Generated by Django 5.0.3 on 2024-03-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_content_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_pdf',
            field=models.FileField(blank=True, null=True, upload_to='products/product_pdf/'),
        ),
    ]
