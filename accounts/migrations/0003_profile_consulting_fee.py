# Generated by Django 3.2.10 on 2022-01-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Consulting_Fee',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
