# Generated by Django 5.0.3 on 2024-04-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayStarApp', '0003_rename_babybringer_baby_baby_bringer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baby',
            name='time_of_arrival',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]