# Generated by Django 4.2.7 on 2024-01-14 23:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ticketing", "0005_ticket_tenant_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="entry_permission",
            field=models.BooleanField(default=False),
        ),
    ]
