from django.urls import path
from users.views import UserView, AdminView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('admin/', AdminView.as_view()),
]