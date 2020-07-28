from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, BookSection, BlogComment
from blog import views
import json
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.models import User


# for GET TO WORK PROPERLY
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.blogHome = reverse('blogHome')
        self.blogPost = reverse('blogPost',args=['some-slug'])
        self.post_stuff = Post.objects.create(
            title='something',
            author='someone',
            brief='thisIsBrief',
            content='thisIsContent',
            slug='some-slug',
        )
        # for comment
        self.myuser = User.objects.create_user(username='john', email='john@sm.co', password='smith' )
        self.br = {'loginusername': 'john', 'loginpassword': 'smith'}
        self.user = authenticate(username=self.br['loginusername'],password=self.br['loginpassword'])
        self.post_comment = BlogComment.objects.create(
                comment='this is the comment for testing purpose',
                user= User.objects.get(username='john'),
                post= self.post_stuff,
            )
        # for reply
        self.myuser1 = User.objects.create_user(username='joh', email='joh@sm.co', password='smih' )
        self.br1 = {'loginusername': 'joh', 'loginpassword': 'smih'}
        self.user1 = authenticate(username= self.br1['loginusername'],password= self.br1['loginpassword'])
        self.reply_info = BlogComment.objects.create(
                    comment='this is the comment reply for testing purpose',
                    user= User.objects.get(username='joh'),
                    post= self.post_stuff,
                    parent = BlogComment.objects.get(sno=self.post_comment.sno),
                )
        self.about = reverse('about')
        self.archive = reverse('archive')
        self.books = reverse('books')
        self.contact = reverse('contact')
        self.home = reverse('home')

        self.handleLogin = reverse('handleLogin')
        self.handleLogout = reverse('handleLogout')
        self.handleSignup = reverse('handleSignup')

    def test_blogHome_GET(self):
        response = self.client.get(self.blogHome)

        self.assertEqual(response.status_code, 200 )
        self.assertTemplateUsed(response,'blog/blogHome.html', 'base.html')
    def test_blogPost_GET(self):
        response = self.client.get(self.blogPost)

        self.assertEqual(response.status_code, 200 )
        self.assertTemplateUsed(response,'blog/blogPost.html', 'base.html')
        self.assertEquals(self.post_stuff.title,'something')
        self.assertEquals(self.post_stuff.author,'someone')
        self.assertEquals(self.post_stuff.content,'thisIsContent')


    def test_about_GET(self):
        response = self.client.get(self.about)

        self.assertEqual(response.status_code, 200 )
        self.assertTemplateUsed(response,'home/about.html', 'base.html')
    def test_archive_GET(self):
        response = self.client.get(self.archive)

        self.assertEqual(response.status_code, 200 )
        self.assertTemplateUsed(response,'home/archive.html', 'base.html')
    def test_books_GET(self):
        response = self.client.get(self.books )

        self.assertEqual(response.status_code, 200 )
        self.assertTemplateUsed(response,'home/books.html', 'base.html')
    def test_contact_GET(self):
        response = self.client.get(self.contact)

        self.assertEqual(response.status_code, 200 )
        self.assertTemplateUsed(response,'home/contact.html', 'base.html')
    def test_home_GET(self):
        response = self.client.get(self.home)

        self.assertEqual(response.status_code, 200 )
        self.assertTemplateUsed(response,'home/Home.html', 'base.html')
    # this is awesome test case 
    def test_search_GET(self):
        search = reverse('search') 
        response = self.client.get(search,{'query':'hayat'})

        self.assertEqual(response.status_code, 200 )
        self.assertEqual(response.context[-1]['query'], 'hayat' )
        self.assertTemplateUsed(response,'home/search.html', 'base.html')
    

    def test_for_handleLogin_Post(self):
        response = self.client.post(self.handleLogin, {'loginusername': 'john', 'loginpassword': 'smith'})
        
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response,'base.html')


    def test_for_handleLogout_Post(self):
        response = self.client.post(self.handleLogout)
        self.assertEqual(response.status_code, 302)
    
    def test_for_handleLogout_Post(self):
        response = self.client.post(self.handleSignup, {'username':'someName',
        'email1':'some@one.com',
        'pass1':'somepassword',
        'pass2':'somepassword',

        })
        self.assertEqual(response.status_code, 302)

    # this is awesome test case 
    def test_for_comment_posting(self):
        if self.user is not None:
            response = self.client.get(self.blogPost)

            self.assertEqual(response.status_code, 200)    
            self.assertEquals(self.post_comment.comment,'this is the comment for testing purpose')
            self.assertEquals(self.post_comment.user.get_username(), self.br['loginusername'])
            self.assertEquals(self.post_comment.post,self.post_stuff)    

    def test_for_reply_posting(self):
        if self.user1 is not None:
            response = self.client.get(self.blogPost)

            self.assertEqual(response.status_code, 200)    
            self.assertEquals(self.reply_info.comment,'this is the comment reply for testing purpose')
            self.assertEquals(self.reply_info.user.get_username(),self.br1['loginusername'])
            self.assertEquals(self.reply_info.post,self.post_stuff)
            self.assertEquals(self.reply_info.parent,self.post_comment)


# views for topic_sub is left over
