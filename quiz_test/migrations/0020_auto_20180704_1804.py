# Generated by Django 2.0.5 on 2018-07-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_test', '0019_test_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
