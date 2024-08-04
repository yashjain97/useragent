from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Agent
from api.serializers import AgentSerializer, CreateAgentSerializer, AgentRunValidationSerializer, \
    AgentRunCreateSerializer


class AgentView(ListCreateAPIView, RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()
    lookup_field = 'agent_id'

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AgentSerializer
        elif self.request.method == "POST":
            return CreateAgentSerializer

    def get(self, request, *args, **kwargs):
        agent_id = self.kwargs.get('agent_id', None)
        if agent_id:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer_class()(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgentRunCreateView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AgentRunValidationSerializer

    def post(self, request):
        request.data["user"] = request.user.id
        validation_serializer = self.serializer_class(data=request.data)
        if not validation_serializer.is_valid():
            return Response(validation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = AgentRunCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
