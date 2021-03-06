# Generated by Django 3.0.8 on 2020-07-17 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_auto_20200717_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.Category'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.TextField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=50),
        ),
    ]
