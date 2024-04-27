# Generated by Django 5.0.3 on 2024-04-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('babyNum', models.IntegerField()),
                ('babyBringer', models.CharField(max_length=100)),
                ('parentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=13)),
            ],
        ),
    ]