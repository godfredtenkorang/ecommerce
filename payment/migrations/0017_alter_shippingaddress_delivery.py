# Generated by Django 4.1 on 2024-04-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0016_alter_shippingaddress_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='delivery',
            field=models.CharField(default='International', max_length=50),
        ),
    ]
