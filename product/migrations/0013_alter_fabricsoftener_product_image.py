# Generated by Django 4.1 on 2022-12-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_traders_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricsoftener',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
