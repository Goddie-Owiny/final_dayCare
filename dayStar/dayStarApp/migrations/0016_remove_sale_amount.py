# Generated by Django 5.0.3 on 2024-05-02 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0015_sale_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='amount',
        ),
    ]
