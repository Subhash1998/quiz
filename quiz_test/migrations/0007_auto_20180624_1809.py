# Generated by Django 2.0.5 on 2018-06-24 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_test', '0006_auto_20180624_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz_test.City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz_test.Country'),
        ),
    ]