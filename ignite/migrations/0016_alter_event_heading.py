# Generated by Django 4.1.1 on 2023-05-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ignite', '0015_alter_result_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='heading',
            field=models.CharField(max_length=50),
        ),
    ]