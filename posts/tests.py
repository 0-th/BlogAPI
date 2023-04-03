from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@mail.com',
            password='secret',
        )

        cls.post = Post.objects.create(
            title='Test title',
            author=cls.user,
            body='Test body'
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, 'Test title')
        self.assertEqual(self.post.body, 'Test body')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(str(self.post), 'Test title')
        self.assertEqual(Post.objects.count(), 1)
