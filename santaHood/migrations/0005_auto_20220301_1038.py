# Generated by Django 3.0.1 on 2022-03-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santaHood', '0004_auto_20220301_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='alt',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='santaHood/static/santaHood/img/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]