# Generated by Django 4.2 on 2023-05-09 20:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0016_apikeypermissions_community_allo_scorer_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="community",
            old_name="allo_scorer_id",
            new_name="external_scorer_id",
        ),
    ]
