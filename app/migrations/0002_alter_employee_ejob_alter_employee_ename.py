# Generated by Django 4.2.7 on 2023-11-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EJob',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EName',
            field=models.CharField(max_length=100),
        ),
    ]
