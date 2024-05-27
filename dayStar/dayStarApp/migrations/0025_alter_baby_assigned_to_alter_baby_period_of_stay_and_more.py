# Generated by Django 5.0.3 on 2024-05-20 14:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0024_rename_amount_babypayment_total_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='assigned_To',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.sitter_on_duty'),
        ),
        migrations.AlterField(
            model_name='baby',
            name='period_of_stay',
            field=models.CharField(choices=[('Full Day', 'Full Day'), ('Half Day', 'Half Day')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='babypayment',
            name='baby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.baby'),
        ),
        migrations.AlterField(
            model_name='babypayment',
            name='period_of_stay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.period'),
        ),
        migrations.AlterField(
            model_name='babypayment',
            name='total_Fee',
            field=models.IntegerField(choices=[(10000, '10000'), (15000, '15000'), (300000, '300000'), (450000, '450000')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='next_of_kin',
            field=models.CharField(default=None, max_length=200, validators=[django.core.validators.RegexValidator(message='Enter both names with no special characters', regex="^(?=.{1,100}$)[A-Za-z]+(?:[\\'\\s-][A-Za-z]+)* [A-Za-z]+(?:[\\'\\s-][A-Za-z]+)*$")]),
        ),
        migrations.AlterField(
            model_name='sitterpayment',
            name='sitter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.sitter_on_duty'),
        ),
    ]