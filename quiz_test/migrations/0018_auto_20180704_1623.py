# Generated by Django 2.0.5 on 2018-07-04 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_test', '0017_category_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='question_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='question_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='question_level',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='question_type',
            new_name='q_type',
        ),
    ]
