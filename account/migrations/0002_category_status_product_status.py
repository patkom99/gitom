# Generated by Django 4.1.3 on 2022-12-24 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False, help_text='0-default,1-hidden'),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False, help_text='0-default,1-hidden'),
        ),
    ]