# Generated by Django 5.0.3 on 2024-05-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0009_itemselling_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemselling',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
