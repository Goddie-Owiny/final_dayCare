# Generated by Django 5.0.3 on 2024-04-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0005_remove_baby_time_of_arrival_sitter_nin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='NIN',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
