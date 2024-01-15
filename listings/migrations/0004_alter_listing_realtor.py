# Generated by Django 4.2.7 on 2023-11-22 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0003_remove_listing_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtors.realtor'),
        ),
    ]
