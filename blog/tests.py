from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="ana", password="ClaveSegura123")
        self.post = Post.objects.create(title="Una idea", content="Contenido de prueba", author=self.user)

    def test_home_and_detail_are_public(self):
        self.assertEqual(self.client.get(reverse("post_list")).status_code, 200)
        self.assertEqual(self.client.get(reverse("post_detail", args=[self.post.pk])).status_code, 200)

    def test_create_requires_login(self):
        response = self.client.get(reverse("post_create"))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('post_create')}")

    def test_authenticated_user_can_create_post(self):
        self.client.login(username="ana", password="ClaveSegura123")
        response = self.client.post(reverse("post_create"), {"title": "Nuevo post", "content": "Texto nuevo"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="Nuevo post", author=self.user).exists())

    def test_registration_creates_user(self):
        response = self.client.post(reverse("register"), {
            "username": "luz", "email": "luz@example.com", "password1": "OtraClaveSegura123", "password2": "OtraClaveSegura123",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="luz").exists())
