# Generated by Django 5.0.5 on 2024-10-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_shippingfee_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
