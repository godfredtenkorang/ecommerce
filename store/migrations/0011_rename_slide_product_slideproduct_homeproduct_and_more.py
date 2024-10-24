# Generated by Django 5.0.5 on 2024-05-10 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_home_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Slide_Product',
            new_name='SlideProduct',
        ),
        migrations.CreateModel(
            name='HomeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('brand', models.CharField(default='un-branded', max_length=250)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image', models.ImageField(upload_to='images/home/')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homeproduct', to='store.category')),
            ],
            options={
                'verbose_name_plural': 'home products',
            },
        ),
        migrations.DeleteModel(
            name='Home_Product',
        ),
    ]
