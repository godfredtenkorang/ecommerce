# Generated by Django 4.1 on 2024-03-09 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0012_shippingaddress_delivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='delivery',
        ),
    ]
