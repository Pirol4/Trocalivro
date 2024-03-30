# Generated by Django 5.0.3 on 2024-03-27 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_address_owner_user_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='owner_address',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user'),
            preserve_default=False,
        ),
    ]
