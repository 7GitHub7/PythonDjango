from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blog.views import about,PostListView

class TestUrls(SimpleTestCase):

    def test_blog_about_url_is_resolved(self):
        url = reverse('blog-about')
        print(resolve(url))
        self.assertEquals(resolve(url).func,about)

    def test_blog_home_url_is_resolved(self):
        url = reverse('blog-home',args=['test'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__,PostListView.as_view().__name__)