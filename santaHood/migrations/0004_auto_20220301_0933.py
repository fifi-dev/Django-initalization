# Generated by Django 3.0.1 on 2022-03-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santaHood', '0003_auto_20220301_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='alt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='santaHood/static/santaHood/img/'),
        ),
    ]
