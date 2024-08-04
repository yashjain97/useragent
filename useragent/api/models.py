import uuid

from django.db import models

from accounts.models import User


class Agent(models.Model):
    agent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    imageUrl = models.URLField(max_length=2000, null=True, blank=True)
    redirectUrl = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    prompt_template = models.TextField(null=False)
    prompt_template2 = models.TextField(null=False)
    prompt_template3 = models.TextField(null=False)
    prompt_template4 = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AgentForm(models.Model):
    form_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    form_name = models.CharField(max_length=255, null=False)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="agent_form")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.form_name


class AgentFormField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text'),
        ('textarea', 'Textarea'),
        ('email', 'Email'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('url', 'URL'),
        ('select', 'Select'),
        ('checkbox', 'Checkbox'),
        ('radio', 'Radio'),
        ('password', 'Password'),

    ]

    field_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    form = models.ForeignKey(AgentForm, on_delete=models.CASCADE, related_name="form_fields")
    label = models.CharField(max_length=255, null=False)
    placeholder = models.CharField(max_length=255, null=True, blank=True)
    input_type = models.CharField(max_length=50, choices=FIELD_TYPES, default='text')
    required = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.form.form_name}  -  {self.input_type}'


class AgentRun(models.Model):
    run_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_run")
    agent = models.ForeignKey(Agent, to_field="agent_id", on_delete=models.CASCADE, related_name="agent_run")
    request = models.JSONField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['agent']),
        ]

    def __str__(self):
        return f'{self.user}  -  {self.agent} -  {self.run_id}'
