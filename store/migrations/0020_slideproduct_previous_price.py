# Generated by Django 5.0.5 on 2024-06-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_reviewcomment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideproduct',
            name='previous_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True),
        ),
    ]
