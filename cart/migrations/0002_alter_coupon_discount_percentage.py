# Generated by Django 5.0.5 on 2024-10-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount_percentage',
            field=models.IntegerField(max_length=3),
        ),
    ]