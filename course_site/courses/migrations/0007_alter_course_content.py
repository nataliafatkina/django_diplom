# Generated by Django 5.1.4 on 2025-01-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
