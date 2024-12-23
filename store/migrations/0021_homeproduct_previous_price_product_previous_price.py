# Generated by Django 5.0.5 on 2024-06-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_slideproduct_previous_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeproduct',
            name='previous_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='previous_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True),
        ),
    ]
