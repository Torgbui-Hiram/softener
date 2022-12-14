# Generated by Django 4.1 on 2022-08-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FabricSoftener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('image_url', models.ImageField(upload_to='')),
                ('price', models.URLField()),
                ('stock', models.CharField(max_length=2083)),
            ],
        ),
    ]
