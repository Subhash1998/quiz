# Generated by Django 2.0.5 on 2018-07-05 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_test', '0024_auto_20180705_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
