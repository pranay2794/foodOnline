# Generated by Django 5.1.3 on 2024-11-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_license',
            field=models.ImageField(upload_to='vendor/license'),
        ),
    ]
