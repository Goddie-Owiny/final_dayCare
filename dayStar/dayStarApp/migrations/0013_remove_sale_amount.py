# Generated by Django 5.0.3 on 2024-04-30 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0012_alter_sale_quantity_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='amount',
        ),
    ]