# Generated by Django 4.1.1 on 2022-09-06 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gender",
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
                ("gender", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("first_name", models.CharField(blank=True, max_length=100, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "middle_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("birthday", models.DateField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "gender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.gender"
                    ),
                ),
            ],
        ),
    ]
