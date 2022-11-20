# Generated by Django 4.1.3 on 2022-11-19 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_alter_user_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                blank=True, default="avatar.svg", null=True, upload_to="images"
            ),
        ),
    ]
