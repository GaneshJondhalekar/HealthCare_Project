# Generated by Django 3.2.20 on 2023-07-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pharma', '0002_pharma_is_pharma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharma',
            name='is_pharma',
        ),
        migrations.AddField(
            model_name='pharma',
            name='user_type',
            field=models.CharField(default='pharma', max_length=10),
        ),
    ]