# Generated by Django 3.0.1 on 2022-03-01 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santaHood', '0005_auto_20220301_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
