from django.test import TestCase
from follows.models import Follow
from login.models import CustomUser

class FollowModelTest(TestCase):
    def test_create_follow(self):
        # Corrigido: removido o campo 'username'
        follower = CustomUser.objects.create_user(email="follower@example.com", password="testpass")
        followed = CustomUser.objects.create_user(email="followed@example.com", password="testpass")
        
        # Criando o relacionamento de follow
        follow = Follow.objects.create(follower=follower, followed=followed)
        
        # Verificando se o follower está correto
        self.assertEqual(follow.follower, follower)
