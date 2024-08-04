from django.urls import path

from api.views import AgentView, AgentRunCreateView

urlpatterns = [
    path('agents', AgentView.as_view(), name='agents'),
    path('agents/<uuid:agent_id>/', AgentView.as_view(), name='agent-detail'),
    path('agent/run/', AgentRunCreateView.as_view(), name='agent-run-create'),

]
