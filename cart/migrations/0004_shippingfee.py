# Generated by Django 5.0.5 on 2024-10-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_coupon_discount_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('fee', models.IntegerField()),
            ],
        ),
    ]