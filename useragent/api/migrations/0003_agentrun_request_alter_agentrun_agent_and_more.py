# Generated by Django 5.0.7 on 2024-08-03 13:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_agentformfield_input_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="agentrun",
            name="request",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="agentrun",
            name="agent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="agent_run",
                to="api.agent",
            ),
        ),
        migrations.AlterField(
            model_name="agentrun",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_run",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="AgentMetadata",
        ),
    ]