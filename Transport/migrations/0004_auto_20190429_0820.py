# Generated by Django 2.0.7 on 2019-04-29 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Transport', '0003_auto_20190429_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='Bus_Model',
            new_name='Model',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='Car_Model',
            new_name='Model',
        ),
        migrations.RenameField(
            model_name='truck',
            old_name='Truck_Model',
            new_name='Model',
        ),
    ]
