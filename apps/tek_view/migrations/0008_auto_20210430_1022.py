# Generated by Django 2.2.4 on 2021-04-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tek_view', '0007_power'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pump_one',
            name='pressure_in',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pump_one',
            name='pressure_out',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pump_three',
            name='pressure_in',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pump_three',
            name='pressure_out',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pump_two',
            name='pressure_in',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pump_two',
            name='pressure_out',
            field=models.FloatField(default=0),
        ),
    ]
