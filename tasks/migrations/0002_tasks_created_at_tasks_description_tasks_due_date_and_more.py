# Generated by Django 5.0.3 on 2024-03-11 05:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=20),
        ),
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('to-do', 'To Do'), ('completed', 'Completed'), ('blocked', 'Blocked')], default='to-do', max_length=20),
        ),
        migrations.AddField(
            model_name='tasks',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]