# Generated by Django 3.0.8 on 2020-07-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_auto_20200717_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.TextField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')], max_length=50),
        ),
    ]
