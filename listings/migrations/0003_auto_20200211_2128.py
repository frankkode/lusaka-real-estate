# Generated by Django 3.0.3 on 2020-02-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_swimming_pool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='swimming_pool',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]
