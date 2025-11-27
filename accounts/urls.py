
from django.urls import path
from .views_exemplo import profile
from django.http import JsonResponse

def login_placeholder(request):
    return JsonResponse({'detail': 'Login via API/JWT. Use o endpoint de autenticação.'}, status=401)

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("login/", login_placeholder, name="login"),
]
