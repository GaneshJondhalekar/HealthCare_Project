# Generated by Django 3.2.20 on 2023-07-19 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Patients', '0003_auto_20230719_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Patient_group',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='groups',
        ),
        migrations.AddField(
            model_name='patient',
            name='groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_patients', to='auth.group'),
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='patient',
            name='user_permissions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permissions_patients', to='auth.permission'),
        ),
    ]
