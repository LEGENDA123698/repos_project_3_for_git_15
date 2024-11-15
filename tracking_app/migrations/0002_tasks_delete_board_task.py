# Generated by Django 5.1.2 on 2024-10-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('todo', 'Need to do'), ('in_progress', 'In Development'), ('completed', 'Completed')], default='todo', max_length=20)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=20)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Board_Task',
        ),
    ]
