# Generated by Django 4.2.6 on 2024-03-15 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("registry", "0031_stakeevent_stake"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Stake",
        ),
        migrations.DeleteModel(
            name="StakeEvent",
        ),
    ]
