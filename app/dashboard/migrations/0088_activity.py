# Generated by Django 2.0.6 on 2018-06-30 22:24

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0087_auto_20180621_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('activity_type', models.CharField(blank=True, choices=[('new_bounty', 'New Bounty'), ('start_work', 'Work Started'), ('stop_work', 'Work Stopped'), ('work_submitted', 'Work Submitted'), ('work_done', 'Work Done'), ('worker_approved', 'Worker Approved'), ('worker_rejected', 'Worker Rejected'), ('worker_applied', 'Worker Applied'), ('increased_bounty', 'Increased Funding'), ('killed_bounty', 'Canceled Bounty'), ('new_tip', 'New Tip'), ('receive_tip', 'Tip Received')], max_length=50)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('bounty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='dashboard.Bounty')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='dashboard.Profile')),
                ('tip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='dashboard.Tip')),
            ],
        ),
    ]