# Generated by Django 5.0.3 on 2024-05-09 15:30

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0002_baby_period_of_stay_sale_baby_alter_baby_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name='Sitter_on_duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('on_duty', 'on_duty')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('sitter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.sitter')),
            ],
        ),
        migrations.AddField(
            model_name='baby',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dayStarApp.sitter_on_duty'),
        ),
    ]
