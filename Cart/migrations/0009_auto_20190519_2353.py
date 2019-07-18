# Generated by Django 2.0.7 on 2019-05-19 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0008_auto_20190514_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100, null=True),
        ),
    ]