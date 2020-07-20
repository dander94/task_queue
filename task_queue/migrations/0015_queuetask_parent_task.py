# Generated by Django 3.0.4 on 2020-04-21 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_queue', '0014_auto_20200415_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='queuetask',
            name='parent_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_tasks', to='task_queue.QueueTask', verbose_name='Parent Task'),
        ),
    ]
