# Generated by Django 3.2.18 on 2023-07-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField()),
                ('overdue', models.BooleanField(default=False)),
                ('task_owners', models.JSONField(blank=True, default=list)),
                ('priority', models.PositiveIntegerField(default=1)),
                ('state', models.CharField(max_length=15)),
            ],
        ),
    ]