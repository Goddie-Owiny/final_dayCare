# Generated by Django 5.0.3 on 2024-05-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0003_alter_sitter_nin_alter_sitter_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemselling',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=5000, max_digits=10, null=True),
        ),
    ]