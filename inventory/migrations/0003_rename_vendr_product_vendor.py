# Generated by Django 4.2.3 on 2023-07-07 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_vendr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='vendr',
            new_name='vendor',
        ),
    ]
