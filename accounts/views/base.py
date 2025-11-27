from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from accounts.models import User_Groups, Group_Permissions
from companies.models import Company


class Base(APIView):
    def get_enterprise_user(self, user_id):
        """
        Retorna o contexto de permissões do usuário na empresa.

        Parâmetros:
            user_id (int): ID do usuário a ser consultado.

        Retorno:
            dict: {
                'is_owner': bool,
                'permissions': [
                    {'id': int, 'label': str, 'codename': str}, ...
                ]
            }
        """
        # Verifica se o usuário é proprietário de alguma empresa
        is_owner = Company.objects.filter(owner_id=user_id).exists()
        if is_owner:
            return {
                "is_owner": True,
                "permissions": []
            }

        # Busca todos os grupos do usuário
        groups = User_Groups.objects.filter(user_id=user_id).select_related('group')
        if not groups.exists():
            # Usuário não pertence a nenhum grupo, logo não tem permissões
            return {
                "is_owner": False,
                "permissions": []
            }

        permissions_set = set()
        permissions_list = []

        for user_group in groups:
            # Busca permissões associadas ao grupo
            group_permissions = Group_Permissions.objects.filter(group_id=user_group.group.id)
            for perm in group_permissions:
                # Suporte a diferentes estruturas de permission
                permission_obj = getattr(perm, 'permission', None)
                if permission_obj:
                    perm_id = getattr(permission_obj, 'id', None)
                    perm_label = getattr(permission_obj, 'name', None)
                    perm_codename = getattr(permission_obj, 'codename', None)
                else:
                    # Fallback para campos diretos
                    perm_id = getattr(perm, 'id', None)
                    perm_label = getattr(perm, 'permission_name', None)
                    perm_codename = getattr(perm, 'permission_name', None)

                # Evita permissões duplicadas
                perm_tuple = (perm_id, perm_label, perm_codename)
                if perm_tuple not in permissions_set:
                    permissions_set.add(perm_tuple)
                    permissions_list.append({
                        "id": perm_id,
                        "label": perm_label,
                        "codename": perm_codename
                    })

        return {
            "is_owner": False,
            "permissions": permissions_list
        }


