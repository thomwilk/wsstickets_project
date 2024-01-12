# Generated by Django 4.2.7 on 2023-12-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ticketing", "0003_ticket_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="status",
            field=models.CharField(
                choices=[
                    ("Open", "Open"),
                    ("In Progress", "In Progress"),
                    ("Closed", "Closed"),
                ],
                default="open",
                max_length=12,
            ),
        ),
    ]
