from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.models import APIKey
from rest_framework.permissions import IsAuthenticated
from .models import Content
from .serializers import ContentSerializer
from .permissions import IsEditor

# API to generate API Key
class GenerateAPIKey(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        api_key, key = APIKey.objects.create_key(
            name=f"{request.user.username}-key"
        )
        return Response({"api_key": key})


# Protected API
class ContentAPI(APIView):
    permission_classes = [IsAuthenticated, IsEditor]

    def get(self, request):
        content = Content.objects.first()
        serializer = ContentSerializer(content)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# Frontend View
def home(request):
    content = Content.objects.first()
    return render(request, 'home.html', {'content': content})


def update_content(request):
    content = Content.objects.first()
    if request.method == 'POST':
        content.title = request.POST['title']
        content.body = request.POST['body']
        content.save()
        return redirect('/')
