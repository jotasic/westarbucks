# Generated by Django 3.2.3 on 2021-05-23 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_nutrition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ategory', to='products.menu'),
        ),
    ]
