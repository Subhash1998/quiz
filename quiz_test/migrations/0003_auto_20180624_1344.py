# Generated by Django 2.0.5 on 2018-06-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_test', '0002_auto_20180624_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]