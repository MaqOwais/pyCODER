from django.test import TestCase
from blog.models import Post, BookSection, BlogComment, Topic
from home.models import Contact
from django.core.files import File
from django.contrib.auth.models import User

# from django.core.files.uploadedfile import SimpleUploadedFile

# not  included photos and pdf files

class TestModels(TestCase):

    def setUp(self):

        self.topic1 = Topic.objects.create(name='anyname')

        self.post1 = Post.objects.create(
            title='thsi is title',
            author='someone',
            brief='this is brief',
            content='this is some content',
            slug='some-slug',
            topicsub= Topic.objects.get(name=self.topic1.name)
            # BlogComment.objects.get(sno=self.post_comment.sno),
        )
        self.book1 = BookSection.objects.create(
            BookTitle='anybook',
            Author='anyone',
            BookDescription='thsi is description',
        )

    def test_for_Topic_selection(self):
        self.assertEquals(self.topic1.name,'anyname')

    def test_Blogpost_while_posting(self):
        self.assertEquals(self.post1.slug,'some-slug')
        self.assertEquals(self.post1.author,'someone')
        self.assertEquals(self.post1.brief,'this is brief')
        self.assertEquals(self.post1.content,'this is some content')
        self.assertEquals(self.post1.title,'thsi is title')
        self.assertEquals(self.post1.topicsub.name,'anyname')
        self.post1.delete()

    def test_for_book_posting(self):
        

        self.assertEquals(self.book1.BookTitle,'anybook')
        self.assertEquals(self.book1.Author,'anyone')
        self.assertEquals(self.book1.BookDescription,'thsi is description')
        self.book1.delete()

    def test_for_contact_posting(self):
        contact_info = Contact.objects.create(
            name='anyone_contact',
            phone='899899899899',
            email='anyone@email.com',
            content='thsi is message to admin',

        )

        self.assertEquals(contact_info.name,'anyone_contact')
        self.assertEquals(contact_info.phone,'899899899899')
        self.assertEquals(contact_info.email,'anyone@email.com')
        self.assertEquals(contact_info.content,'thsi is message to admin')
        contact_info.delete()

# for image and book file
class SimpleTest(TestCase):

    def test_for_BookImage(self):   
        book3 = BookSection()
        book3.Image = File(open("static/sho.png",'rb'))
        book3.save()
        for e in BookSection.objects.all():
            pr= e.Image
        p = pr.path
        self.failUnless(open(p), 'file not found')
        book3.Image.delete()
        book3.delete()

    def test_for_BookFile(self):  
        book3 = BookSection()
        book3.BookFile = File(open("static/dummy.pdf",'rb'))
        book3.save()
        for e in BookSection.objects.all():
            pr= e.BookFile
        p = pr.path
        self.failUnless(open(p), 'file not found')
        book3.BookFile.delete()
        book3.delete()

