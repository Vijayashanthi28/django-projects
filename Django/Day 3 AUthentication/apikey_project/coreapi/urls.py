from django.urls import path
from coreapi.views import EditorOnlyAPIView

urlpatterns = [
    path('editor-api/', EditorOnlyAPIView.as_view()),
]