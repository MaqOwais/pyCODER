from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from blog.views import postComment, blogHome, blogPost
from home.views import home, topic_page, archive, about, books, contact, search, handleSignup, handleLogin, handleLogout

# from .models import Post

# Create your tests here.


# test cases for urls resolution (working)
class TestUrls(SimpleTestCase):

    def test_postComment_urls_are_resolved(self):
        url = reverse('postComment')
        self.assertEqual(resolve(url).func, postComment)
    def test_blogHome_urls_are_resolved(self):
        url = reverse('blogHome')
        self.assertEqual(resolve(url).func, blogHome)
    def test_blogPost_urls_are_resolved(self):
        url = reverse('blogPost', args=['some-slug'])
        self.assertEqual(resolve(url).func, blogPost)
    def test_topic_page_urls_are_resolved(self):
        url = reverse('topic_page', args=['some-toic'])
        self.assertEqual(resolve(url).func, topic_page)

    
    def test_home_urls_are_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)
    def test_archive_urls_are_resolved(self):
        url = reverse('archive')
        self.assertEqual(resolve(url).func, archive)
    def test_about_urls_are_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)
    def test_books_urls_are_resolved(self):
        url = reverse('books')
        self.assertEqual(resolve(url).func, books)
    def test_contact_urls_are_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)
    def test_search_urls_are_resolved(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)
    def test_handleSignup_urls_are_resolved(self):
        url = reverse('handleSignup')
        self.assertEqual(resolve(url).func, handleSignup)
    def test_handleLogin_urls_are_resolved(self):
        url = reverse('handleLogin')
        self.assertEqual(resolve(url).func, handleLogin)
    def test_handleLogout_urls_are_resolved(self):
        url = reverse('handleLogout')
        self.assertEqual(resolve(url).func, handleLogout)


