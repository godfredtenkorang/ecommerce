# Generated by Django 4.1 on 2024-04-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0021_alter_shippingaddress_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='delivery',
            field=models.CharField(choices=[('International', 'International'), ('Domestic', 'Domestic')], default='International', max_length=50),
        ),
    ]
