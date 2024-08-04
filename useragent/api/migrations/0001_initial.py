# Generated by Django 5.0.7 on 2024-08-03 11:35

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Agent",
            fields=[
                (
                    "agent_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("imageUrl", models.URLField(blank=True, max_length=2000, null=True)),
                (
                    "redirectUrl",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("prompt_template", models.TextField()),
                ("prompt_template2", models.TextField()),
                ("prompt_template3", models.TextField()),
                ("prompt_template4", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="AgentForm",
            fields=[
                (
                    "form_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("form_name", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agent_form",
                        to="api.agent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AgentFormField",
            fields=[
                (
                    "field_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("label", models.CharField(max_length=255)),
                (
                    "placeholder",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "input_type",
                    models.CharField(
                        choices=[
                            ("text", "Text"),
                            ("textarea", "Textarea"),
                            ("email", "Email"),
                            ("number", "Number"),
                            ("date", "Date"),
                            ("url", "URL"),
                            ("select", "Select"),
                            ("checkbox", "Checkbox"),
                            ("radio", "Radio"),
                        ],
                        default="text",
                        max_length=50,
                    ),
                ),
                ("required", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="form_fields",
                        to="api.agentform",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AgentMetadata",
            fields=[
                (
                    "metadata_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("key", models.CharField(max_length=255)),
                ("value", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="formData",
                        to="api.agent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AgentRun",
            fields=[
                (
                    "run_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("response", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.agent"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "indexes": [
                    models.Index(
                        fields=["user"], name="api_agentru_user_id_548716_idx"
                    ),
                    models.Index(
                        fields=["agent"], name="api_agentru_agent_i_8d76dc_idx"
                    ),
                ],
            },
        ),
    ]