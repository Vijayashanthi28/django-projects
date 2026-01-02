from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from coreapi.permissions import IsEditorUser


class EditorOnlyAPIView(APIView):
    permission_classes = [HasAPIKey, IsEditorUser]

    def get(self, request):
        return Response({
            "message": "Hello Editor! You have API key access."
        })