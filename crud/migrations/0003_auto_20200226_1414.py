# Generated by Django 3.0.3 on 2020-02-26 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_productlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productlist',
            old_name='product_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='productlist',
            old_name='product_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='productlist',
            old_name='product_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='productlist',
            old_name='product_title',
            new_name='title',
        ),
    ]
