# Generated by Django 4.1.1 on 2023-02-23 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ignite', '0002_events_results_accomodation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Judges',
            new_name='Judge',
        ),
        migrations.RenameModel(
            old_name='Results',
            new_name='Result',
        ),
    ]