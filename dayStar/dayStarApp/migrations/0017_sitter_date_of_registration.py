# Generated by Django 5.0.3 on 2024-05-18 15:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0016_alter_issue_stock_date_of_issue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitter',
            name='date_of_registration',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
