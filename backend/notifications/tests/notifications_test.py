from django.test import TestCase
from notifications.models import Notification
from login.models import CustomUser
from tweets.models import Tweet

class NotificationModelTest(TestCase):
    def test_create_notification(self):
        # Corrigido: removido o campo 'username'
        user = CustomUser.objects.create_user(email="testuser@example.com", password="testpass")
        
        # Criando a notificação para o usuário
        notification = Notification.objects.create(user=user, content="New follower")
        
        # Verificando o conteúdo da notificação
        self.assertEqual(notification.content, "New follower")
