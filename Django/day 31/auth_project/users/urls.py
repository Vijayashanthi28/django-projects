from django.urls import path
from .views import RegisterUserView, LoginUserView, ProtectedView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginUserView.as_view()),
    path('protected/', ProtectedView.as_view()),
]
