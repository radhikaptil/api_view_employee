# Generated by Django 4.2.7 on 2023-11-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EName', models.CharField(max_length=10)),
                ('ESal', models.IntegerField()),
                ('EJob', models.CharField(max_length=10)),
            ],
        ),
    ]
