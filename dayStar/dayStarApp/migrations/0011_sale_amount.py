# Generated by Django 5.0.3 on 2024-04-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0010_sale_delete_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
