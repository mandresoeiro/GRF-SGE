# -*- coding: utf-8 -*-
from rest_framework.exceptions import AuthenticationFailed, APIException
from django.contrib.auth.hashers import check_password, make_password
from accounts.models import CustomUser
from companies.models import Company


class Authentication:
    """
    Classe responsável por autenticação e cadastro de usuários.
    """

    def signin(self, email=None, password=None) -> CustomUser:
        """
        Realiza o login de um usuário.
        - Verifica se o email existe.
        - Verifica se a senha está correta.
        - Retorna o usuário autenticado ou lança exceção.
        """
        exception_auth = AuthenticationFailed('Email e/ou senha incorreto(s)')

        # Verifica se o email existe
        if not CustomUser.objects.filter(email=email).exists():
            raise exception_auth

        user = CustomUser.objects.filter(email=email).first()

        # Verifica se a senha está correta
        if not check_password(password, user.password):
            raise exception_auth

        return user

    def signup(
        self, name, email, password, type_account='owner', company_id=False
    ) -> CustomUser:
        """
        Realiza o cadastro de um novo usuário.
        - Valida os campos obrigatórios.
        - Cria usuário como owner ou employee.
        - Cria empresa se for owner.
        - Associa funcionário à empresa se for employee.
        """
        if not name or name == '':
            raise APIException('O nome não deve ser null')

        if not email or email == '':
            raise APIException('O email não deve ser null')

        if not password or password == '':
            raise APIException('O password não deve ser null')

        if type_account == 'employee' and not company_id:
            raise APIException('O id da empresa não deve ser null')

        # Verifica se o email já existe
        if CustomUser.objects.filter(email=email).exists():
            raise APIException('Este email já existe na plataforma')

        password_hashed = make_password(password)

        # Cria o usuário
        created_user = CustomUser.objects.create(
            username=email,  # username obrigatório
            email=email,
            password=password_hashed,
            first_name=name,
            is_staff=True if type_account == 'owner' else False,
        )

        # Se for owner, cria uma empresa
        if type_account == 'owner':
            Company.objects.create(
                name='Nome da empresa',
                owner=created_user,
                address='',
                phone='',
                email=email
            )

        # Se for employee, aqui você pode associar a lógica de funcionário
        # Exemplo: criar um Employee se o modelo existir futuramente
        # if type_account == 'employee':
        #     Employee.objects.create(
        #         company_id=company_id,
        #         user=created_user,
        #     )

        return created_user