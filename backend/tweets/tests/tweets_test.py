from django.test import TestCase
from tweets.models import Tweet
from login.models import CustomUser

class TweetModelTest(TestCase):
    def test_create_tweet(self):
        # Corrigido: removido o campo 'username'
        user = CustomUser.objects.create_user(email="testuser@example.com", password="testpass")
        
        # Criando o tweet para o usuário
        tweet = Tweet.objects.create(user=user, content="Hello World")
        
        # Verificando o conteúdo do tweet
        self.assertEqual(tweet.content, "Hello World")
