# Generated by Django 5.0.3 on 2024-05-20 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0026_sitter_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter_on_duty',
            name='sitter_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.sitter'),
        ),
    ]