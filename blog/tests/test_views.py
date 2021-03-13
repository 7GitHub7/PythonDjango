from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
from
import json 

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('blog-home')
        self.detail_url = reverse('post-detail',args = [1])
        self.post = Post.objects.create(
            title = "Blog Post",
            category = "Python",
            content = "test",
            author = User.....
        ) 

    def test_blog_list_GET(self): 
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_blog_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'blog/post-detail.html')
