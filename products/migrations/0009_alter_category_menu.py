# Generated by Django 3.2.3 on 2021-05-23 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_nutrition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
    ]
