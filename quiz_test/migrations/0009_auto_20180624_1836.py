# Generated by Django 2.0.5 on 2018-06-24 18:36

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_test', '0008_auto_20180624_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, to='quiz_test.City'),
        ),
    ]