# Generated by Django 2.2.4 on 2020-01-12 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200112_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultant',
            name='previous_contracts',
        ),
    ]
