# Generated by Django 4.1 on 2023-12-27 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_wishlist_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='wished_product',
            new_name='product',
        ),
    ]
