# Generated by Django 3.1.3 on 2023-09-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spec', '0004_auto_20230910_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_date',
            field=models.DateField(),
        ),
    ]