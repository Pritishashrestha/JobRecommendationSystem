# Generated by Django 3.1 on 2020-10-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobrec', '0003_auto_20201009_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisttable',
            name='jobstatus',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
