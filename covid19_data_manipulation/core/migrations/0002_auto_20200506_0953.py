# Generated by Django 2.2.1 on 2020-05-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryregion',
            name='population',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='countryregion',
            name='province_state',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='active',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='confirmed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='deaths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='recovered',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
