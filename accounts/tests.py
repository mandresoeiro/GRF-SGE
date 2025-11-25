import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_profile_view(client):
    user_model = get_user_model()
    user = user_model.objects.create_user(username='testuser', password='testpass')
    client.force_login(user)
    response = client.get(reverse('profile'))
    assert response.status_code == 200
    assert b'Perfil' in response.content
