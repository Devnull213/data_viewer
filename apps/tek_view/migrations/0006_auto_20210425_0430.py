# Generated by Django 2.2.4 on 2021-04-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tek_view', '0005_auto_20210425_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='ge_one',
            name='state',
            field=models.CharField(choices=[('run', 'run'), ('auto', 'auto'), ('stop', 'stop')], default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ge_two',
            name='state',
            field=models.CharField(choices=[('run', 'run'), ('auto', 'auto'), ('stop', 'stop')], default='auto', max_length=50),
            preserve_default=False,
        ),
    ]
