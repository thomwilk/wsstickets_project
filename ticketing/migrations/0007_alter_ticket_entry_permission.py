# Generated by Django 4.2.7 on 2024-01-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ticketing", "0006_ticket_entry_permission"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="entry_permission",
            field=models.BooleanField(default=True),
        ),
    ]
