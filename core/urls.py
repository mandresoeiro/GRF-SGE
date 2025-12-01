from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Bem-vindo ao backend Django!</h1>")


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.auth_urls")),
    path("api/accounts/", include("accounts.urls")),
    path("api/", include("api.urls")),
    path("dashboard/", include("dashboard.urls")),
]
