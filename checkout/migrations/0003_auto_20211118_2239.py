# Generated by Django 3.2.8 on 2021-11-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20211118_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_basket',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]