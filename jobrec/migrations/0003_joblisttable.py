# Generated by Django 3.1.2 on 2020-10-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobrec', '0002_delete_joblisttable'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoblistTable',
            fields=[
                ('jobid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('advertiserurl', models.CharField(blank=True, max_length=500, null=True)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('jobstatus', models.CharField(blank=True, max_length=100, null=True)),
                ('jobdescription', models.TextField(blank=True, null=True)),
                ('joblocation', models.CharField(blank=True, max_length=200, null=True)),
                ('jobtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
            ],
        ),
    ]