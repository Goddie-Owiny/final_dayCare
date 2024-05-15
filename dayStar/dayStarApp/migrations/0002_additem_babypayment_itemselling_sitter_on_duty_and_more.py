# Generated by Django 5.0.3 on 2024-05-13 23:51

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doll_name', models.CharField(default=None, max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(500)])),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='BabyPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, choices=[(10000, '10000'), (15000, '15000'), (300000, '300000'), (450000, '45000')], default=0, null=True)),
                ('date_of_payment', models.DateTimeField(auto_now_add=True, null=True)),
                ('duration_of_pay', models.CharField(choices=[('Half day', 'Half day'), ('Full Day', 'Full Day'), ('Monthly Full Day', 'Monthly Full Day'), ('Monthly Half Day', 'Monthly Half Day')], max_length=100)),
                ('amount_paid', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(3000)])),
            ],
        ),
        migrations.CreateModel(
            name='ItemSelling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doll_name', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(500)])),
                ('quantity', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sitter_on_duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.BooleanField(blank=True, choices=[(True, 'On Duty'), (False, 'Off Duty')], null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SitterPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_baby', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(6)])),
                ('amount_paid', models.PositiveIntegerField(default=3000)),
            ],
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.RemoveField(
            model_name='sitter',
            name='age',
        ),
        migrations.AddField(
            model_name='baby',
            name='period_of_stay',
            field=models.CharField(blank=True, choices=[('Full Day', 'Full Day'), ('Half Day', 'Half Day')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='baby',
            name='time_in',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='baby',
            name='time_out',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='period',
            field=models.CharField(default='Full Day', max_length=100),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='location',
            field=models.CharField(default='Kabalagala', max_length=100),
        ),
        migrations.AddField(
            model_name='babypayment',
            name='baby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.baby'),
        ),
        migrations.AddField(
            model_name='babypayment',
            name='period_of_stay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.period'),
        ),
        migrations.AddField(
            model_name='itemselling',
            name='baby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.baby'),
        ),
        migrations.AddField(
            model_name='sitter_on_duty',
            name='sitter_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.sitter'),
        ),
        migrations.AddField(
            model_name='baby',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.sitter_on_duty'),
        ),
        migrations.AddField(
            model_name='sitterpayment',
            name='sitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.sitter_on_duty'),
        ),
    ]
