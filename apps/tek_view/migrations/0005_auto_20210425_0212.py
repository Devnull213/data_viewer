# Generated by Django 2.2.4 on 2021-04-25 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tek_view', '0004_pump_one_pump_three_pump_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='pump_one',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pump_three',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pump_two',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
