# Generated by Django 5.0.5 on 2024-05-30 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_reviewcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='store.reviewcomment'),
        ),
    ]
