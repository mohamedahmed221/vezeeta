# Generated by Django 3.2.10 on 2022-01-09 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0015_auto_20220109_0800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='Total',
            new_name='total',
        ),
    ]