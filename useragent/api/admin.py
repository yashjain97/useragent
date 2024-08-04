from django.contrib import admin

from api.models import AgentRun, Agent, AgentForm, AgentFormField

admin.site.register(Agent)
admin.site.register(AgentRun)
admin.site.register(AgentForm)
admin.site.register(AgentFormField)
