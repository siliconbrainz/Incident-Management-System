# Generated by Django 3.0.7 on 2020-06-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drop',
            name='customer_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
