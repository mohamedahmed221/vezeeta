# Generated by Django 3.2.10 on 2022-01-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0008_alter_availabledate_date_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabledate',
            name='date_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
