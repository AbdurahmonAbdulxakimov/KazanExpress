# Generated by Django 4.2.7 on 2024-02-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.ManyToManyField(related_name="users", to="users.role"),
        ),
    ]