# Generated by Django 4.2.6 on 2023-10-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productimage_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='products',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
