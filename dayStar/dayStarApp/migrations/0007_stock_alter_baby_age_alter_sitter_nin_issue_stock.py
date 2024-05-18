# Generated by Django 5.0.3 on 2024-05-15 14:39

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0006_alter_baby_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='baby',
            name='age',
            field=models.PositiveIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(1, message='Baby must be atleast 1 year old'), django.core.validators.MaxValueValidator(6, message='Baby must be between 1 and 6 years old')]),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='NIN',
            field=models.CharField(max_length=14, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(message='Enter a valid Ugandan NIN', regex='^\\d{3}[\\d]{6}[A-Z]\\d{2}$')]),
        ),
        migrations.CreateModel(
            name='Issue_Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('date_of_issue', models.DateTimeField(auto_now_add=True)),
                ('stock_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.stock')),
            ],
        ),
    ]
