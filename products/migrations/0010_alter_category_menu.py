# Generated by Django 3.2.3 on 2021-05-23 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_category_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.menu'),
        ),
    ]
