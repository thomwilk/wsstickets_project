# Generated by Django 4.2.7 on 2024-01-14 23:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ticketing", "0004_alter_ticket_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="tenant_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
