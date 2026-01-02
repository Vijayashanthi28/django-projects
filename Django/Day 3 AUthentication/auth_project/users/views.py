from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Hello, authenticated user!"
        })


class AdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({
            "message": "Hello, admin user!"
        })