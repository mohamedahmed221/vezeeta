# Generated by Django 3.2.10 on 2022-01-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0013_auto_20220109_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='Total',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
