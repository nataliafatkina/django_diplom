# Generated by Django 5.1.4 on 2025-01-14 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='Общая', max_length=50),
        ),
    ]
