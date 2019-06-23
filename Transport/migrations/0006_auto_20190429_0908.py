# Generated by Django 2.0.7 on 2019-04-29 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Transport', '0005_auto_20190429_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoMobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.CharField(max_length=20)),
                ('Color', models.CharField(max_length=10)),
                ('No_of_Seat', models.PositiveIntegerField()),
                ('Air_Condition', models.BooleanField(default=True)),
                ('Availability', models.BooleanField(default=True)),
                ('Cost', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_code', models.CharField(max_length=20)),
                ('Customer', models.CharField(max_length=50)),
                ('From', models.CharField(max_length=50)),
                ('To', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_Name', models.CharField(default='Tesla', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_car', models.BooleanField(default=False)),
                ('is_truck', models.BooleanField(default=False)),
                ('is_Bus', models.BooleanField(default=False)),
                ('is_Tanker', models.BooleanField(default=False)),
                ('tag', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='Vehicle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transport.Vehicle'),
        ),
        migrations.AddField(
            model_name='automobile',
            name='Vehicle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transport.Vehicle'),
        ),
    ]
