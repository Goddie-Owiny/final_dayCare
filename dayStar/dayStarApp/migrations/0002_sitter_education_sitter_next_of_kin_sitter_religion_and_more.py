# Generated by Django 5.0.3 on 2024-04-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitter',
            name='education',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sitter',
            name='next_of_kin',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='sitter',
            name='religion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sitter',
            name='sitter_number',
            field=models.CharField(default=None, max_length=10),
        ),
    ]