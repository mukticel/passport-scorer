# Generated by Django 4.1.7 on 2023-03-27 23:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0012_alter_community_rule"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="privileged",
            field=models.BooleanField(default=False),
        ),
    ]
