# Generated by Django 4.1 on 2023-12-24 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_review_delete_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shipping',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
