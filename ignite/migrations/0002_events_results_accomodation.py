# Generated by Django 4.1.1 on 2023-02-23 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ignite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id of user')),
                ('pgm_name', models.CharField(max_length=30, verbose_name='prog_name')),
                ('stage_id', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='position of candidate')),
                ('grade', models.IntegerField(verbose_name='grade of candidate')),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ignite.registration')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ignite.events')),
                ('j_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ignite.judges')),
            ],
        ),
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_id', models.IntegerField(verbose_name='id')),
                ('place_name', models.CharField(max_length=50, verbose_name='acco place')),
                ('date', models.DateTimeField()),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ignite.registration')),
            ],
        ),
    ]
