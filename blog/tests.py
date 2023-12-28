# blog/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

# blog/tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        Post.objects.create(title='First Post', author=user, content='Just a test post')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_content = f'{post.content}'
        self.assertEqual(expected_title, 'First Post')
        self.assertEqual(expected_content, 'Just a test post')



class PostViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(title='First Post', author=self.user, content='Just a test post')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Just a test post')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First Post')
        self.assertTemplateUsed(response, 'blog/post_detail.html')
