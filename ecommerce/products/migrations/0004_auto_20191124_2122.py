# Generated by Django 2.2.7 on 2019-11-24 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='Title',
        ),
    ]
