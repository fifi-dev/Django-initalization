# Generated by Django 3.0.1 on 2022-03-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santaHood', '0008_auto_20220301_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/santaHood/img/'),
        ),
    ]
