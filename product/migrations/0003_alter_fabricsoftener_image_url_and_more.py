# Generated by Django 4.1 on 2022-08-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_fabricsoftener_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricsoftener',
            name='image_url',
            field=models.CharField(max_length=2083),
        ),
        migrations.AlterField(
            model_name='fabricsoftener',
            name='price',
            field=models.FloatField(max_length=2083),
        ),
    ]
