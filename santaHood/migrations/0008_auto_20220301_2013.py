# Generated by Django 3.0.1 on 2022-03-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santaHood', '0007_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=' '),
        ),
    ]
