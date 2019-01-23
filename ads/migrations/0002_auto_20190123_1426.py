# Generated by Django 2.1.4 on 2019-01-23 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "SELECT create_distributed_table('ads_company', 'id')"
        ),
        migrations.RunSQL(
            "SELECT create_distributed_table('ads_campaign', 'company_id')"
        ),
        migrations.RunSQL(
            "SELECT create_distributed_table('ads_ads', 'company_id')"
        ),

    ]
