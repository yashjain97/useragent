from rest_framework import serializers

from api.models import Agent, AgentForm, AgentFormField, AgentRun


class CreateAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['name', 'description', 'imageUrl', 'redirectUrl']


class AgentFormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentFormField
        fields = ['label', 'placeholder', 'input_type', 'required']


class AgentFormSerializer(serializers.ModelSerializer):
    form_fields = AgentFormFieldSerializer(many=True)

    class Meta:
        model = AgentForm
        fields = ['form_name', 'form_fields']


class AgentSerializer(serializers.ModelSerializer):
    form_details = AgentFormSerializer(many=True, source='agent_form')

    class Meta:
        model = Agent
        fields = ['agent_id', 'name', 'imageUrl', 'redirectUrl', 'description', 'form_details']


class AgentRunValidationSerializer(serializers.ModelSerializer):
    request = serializers.JSONField()

    class Meta:
        model = AgentRun
        fields = ['agent', 'request', 'response']

    def validate_request(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("The 'request' field must be a JSON object.")
        return value


class AgentRunCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentRun
        fields = ['user', 'agent', 'request', 'response']
