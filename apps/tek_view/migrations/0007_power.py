# Generated by Django 2.2.4 on 2021-04-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tek_view', '0006_auto_20210425_0430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kva', models.FloatField()),
                ('kw', models.FloatField()),
                ('kvar', models.FloatField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
