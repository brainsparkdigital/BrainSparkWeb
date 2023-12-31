# Generated by Django 5.0 on 2023-12-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='body',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='details',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
    ]
