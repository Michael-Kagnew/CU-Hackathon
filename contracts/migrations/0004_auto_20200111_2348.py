# Generated by Django 3.0.2 on 2020-01-12 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_client_bio'),
        ('contracts', '0003_auto_20200111_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='applicants',
            field=models.ManyToManyField(blank=True, related_name='applicants', to='profiles.Consultant'),
        ),
        migrations.AddField(
            model_name='contract',
            name='team',
            field=models.ManyToManyField(blank=True, related_name='team', to='profiles.Consultant'),
        ),
    ]
