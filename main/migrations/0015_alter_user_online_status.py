# Generated by Django 4.1.3 on 2022-12-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0014_user_online_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="online_status",
            field=models.BooleanField(default=False),
        ),
    ]