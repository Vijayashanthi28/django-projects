from django.urls import path
from users.views import RegisterUserView, ProtectedView


urlpatterns = [
path('register/', RegisterUserView.as_view(), name='register'),
path('protected/', ProtectedView.as_view(), name='protected'),
]