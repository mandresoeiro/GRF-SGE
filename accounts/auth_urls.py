"""
URLs de autenticação do módulo de usuários.

Este arquivo define as rotas responsáveis por lidar com
processos de login (signin) e criação de conta (signup).
Cada rota aponta para uma class-based view específica
que implementa a lógica correspondente.
"""

from django.urls import path
from .views.signin import Signin
from .views.signup import Signup

# Lista de rotas relacionadas à autenticação de usuários
urlpatterns = [
    # Rota responsável pela página de login
    path('login/', Signin.as_view(), name='login'),

    # Rota responsável pela página de criação de conta
    path('signup/', Signup.as_view(), name='signup'),
]
