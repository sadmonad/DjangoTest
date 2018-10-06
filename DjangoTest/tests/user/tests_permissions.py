from django.test import TestCase, override_settings

from django.contrib.auth.models import User


@override_settings(ALLOWED_HOSTS=['testserver'])
class BloggerTest(TestCase):
    def setUp(self):
        self.username = 'test'
        self.password = '123456'

        self.user = User.objects.create_user(self.username, '', self.password)
        self.user.save()

    def test_non_auth_view_blogger(self):
        response = self.client.get('/bloggers/')
        self.assertRedirects(response, '/accounts/login/')

    def test_auth_no_perms_view_blogger(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/bloggers/')
        self.assertEqual(response.status_code, 403)
