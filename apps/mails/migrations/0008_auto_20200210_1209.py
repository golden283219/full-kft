# Generated by Django 3.0 on 2020-02-10 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mails", "0007_remove_announcement_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="announcementviewmodel",
            options={
                "verbose_name": "Announcement View Report",
                "verbose_name_plural": "Announcement View Reports",
            },
        ),
    ]
