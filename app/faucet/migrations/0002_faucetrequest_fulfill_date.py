# Generated by Django 2.0 on 2018-03-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faucet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucetrequest',
            name='fulfill_date',
            field=models.DateTimeField(null=True),
        ),
    ]
