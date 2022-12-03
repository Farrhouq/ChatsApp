# Generated by Django 4.1.3 on 2022-12-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_alter_user_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                default="email@example.com",
                max_length=200,
                unique=True,
                verbose_name="email address",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                blank=True, default="images/avatar.svg", null=True, upload_to="images/"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                max_length=200, null=True, unique=True, verbose_name="username"
            ),
        ),
    ]