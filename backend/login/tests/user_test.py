from django.test import TestCase
from login.models import CustomUser

class UserModelTest(TestCase):
    def test_create_user(self):
        # Corrigido: removido o campo 'username'
        user = CustomUser.objects.create_user(email="testuser@example.com", password="testpass")
        
        # Verificando se o email foi corretamente atribuído
        self.assertEqual(user.email, "testuser@example.com")
