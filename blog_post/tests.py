from django.urls import reverse

from users.models import User
from django.test import TestCase
from .models import BlogPostModel, Comment, LikeDislike
from django.test import Client

client = Client()


class BlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='yunusboyevfarruxbek@gmail.com')
        self.post = BlogPostModel.objects.create(
            title='Test post',
            slug='Test-post',
            description='shagi',
            created_at='24.05.2023',

        )
        self.comment = Comment.objects.create(
            body='new description',
            owner='shagi',
            post='new post',
            created_at='24.05.2023'
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, 'Test Blog')
        self.assertEqual(self.post.slug, 'test-blog')
        self.assertEqual(self.post.description, 'Test blog body')

    def test_blog_post_create(self):
        url = reverse("post_list_create")
        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 400)
        self.assertEqual(response.data['title'], self.post['title'])

    def test_blog_str_method(self):
        self.assertEqual(str(self.post), 'Test Blog')

    def test_blog_post_update(self):
        url = reverse('post_edit', kwargs={'slug': self.post.slug})
        response = client.put(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 200)

    def test_delete(self):
        self.post.delete()
        self.user.delete()
        self.comment.delete()
