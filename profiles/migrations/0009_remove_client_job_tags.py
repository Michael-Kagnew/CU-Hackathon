# Generated by Django 2.2.4 on 2020-01-12 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_remove_consultant_previous_contracts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='job_tags',
        ),
    ]
