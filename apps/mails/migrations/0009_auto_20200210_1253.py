# Generated by Django 3.0 on 2020-02-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mails", "0008_auto_20200210_1209"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="body",
            field=models.TextField(blank=True, null=True),
        ),
    ]