# Generated by Django 5.0.3 on 2024-05-18 07:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0014_alter_additem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemselling',
            name='amount_paid',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='itemselling',
            name='baby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.baby'),
        ),
        migrations.AlterField(
            model_name='itemselling',
            name='doll_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sitterpayment',
            name='num_of_baby',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(6)]),
        ),
    ]