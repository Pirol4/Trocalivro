# Generated by Django 5.0.3 on 2024-04-17 20:23

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_owner_address_address_owner_book_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]