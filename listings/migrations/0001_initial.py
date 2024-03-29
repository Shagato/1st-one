# Generated by Django 4.2.7 on 2023-11-17 19:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=2000)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=2000)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=3)),
                ('garages', models.IntegerField()),
                ('sqft', models.IntegerField()),
                ('lot_size', models.FloatField()),
                ('photo_main', models.ImageField(blank=True, upload_to=' photos/%y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to=' photos/%y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to=' photos/%y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to=' photos/%y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to=' photos/%y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to=' photos/%y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to=' photos/%y/%m/%d/')),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
                ('realtor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]
