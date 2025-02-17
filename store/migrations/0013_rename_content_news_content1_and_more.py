# Generated by Django 5.0.5 on 2024-05-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='content1',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='image',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='title1',
        ),
        migrations.AddField(
            model_name='news',
            name='content2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='content3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='content4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='content5',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='image2',
            field=models.ImageField(null=True, upload_to='news/img/'),
        ),
        migrations.AddField(
            model_name='news',
            name='image3',
            field=models.ImageField(null=True, upload_to='news/img/'),
        ),
        migrations.AddField(
            model_name='news',
            name='image4',
            field=models.ImageField(null=True, upload_to='news/img/'),
        ),
        migrations.AddField(
            model_name='news',
            name='image5',
            field=models.ImageField(null=True, upload_to='news/img/'),
        ),
        migrations.AddField(
            model_name='news',
            name='title2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title5',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
