from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Topic(models.Model):
    name = models.CharField('Topic Name (use underscores and no spaces)' , blank=True, null=True, max_length=120)
    def __str__(self):
        return self.name

# 
class Post(models.Model):
    MONTHLY_CHOICES = (
        ('JAN', 'JAN',),
        ('FEB', 'FEB',),
        ('MAR', 'MAR',),
        ('APR', 'APR',),
        ('MAY', 'MAY',),
        ('JUN', 'JUN',),
        ('JUL', 'JUL',),
        ('AUG', 'AUG',),
        ('SEPT', 'SEPT',),
        ('OCT', 'OCT',),
        ('NOV', 'NOV',),
        ('DEC', 'DEC',),
    )
    YEARLY_CHOICES = (
        ('2014', '2014',),
        ('2015', '2015',),
        ('2016', '2016',),
        ('2017', '2017',),
        ('2018', '2018',),
        ('2019', '2019',),
        ('2020', '2020',),
        ('2021', '2021',),
        ('2022', '2022',),
        ('2023', '2023',),
        ('2024', '2024',),
        ('2025', '2025',),
        ('2026', '2026',),
        ('2027', '2027',),
        ('2028', '2028',),
        ('2029', '2029',),
        ('2030', '2030',),
        ('2031', '2031',),
        ('2032', '2032',),
        ('2033', '2033',),
        ('2034', '2034',),
        ('2035', '2035',),
        ('2036', '2036',),
        ('2037', '2037',),
        ('2038', '2038',),
        ('2039', '2039',),
        ('2040', '2040',),
    )
    
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    brief = models.TextField(max_length=480,null=True)
    content = models.TextField()
    slug = models.CharField(max_length=130)
    views = models.IntegerField(default=0)
    topicsub = models.ForeignKey(Topic, blank=True, null=True, on_delete=models.CASCADE)
    rewrite_topicsub = models.CharField('Rewrite Topicsub (same as above) exactly {very compulsory} else this will not appear with "Topic section"',max_length=255,null=True,blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
    monthly = models.CharField(
        choices=MONTHLY_CHOICES,
        max_length=20,
        null=True
    )
    yearly= models.CharField(
        choices=YEARLY_CHOICES,
        max_length=30,
        null=True,
    )

    def __str__(self):
        return self.title + ' by ' + self.author

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("blogPost", kwargs={"slug": str(self.slug)})
    # def __unicode__(self):
    #     return self.month + self.year



class BookSection(models.Model):
    sno = models.AutoField(primary_key=True)
    BookTitle = models.CharField(max_length=255)
    Author = models.CharField(max_length=100)
    BookDescription = models.TextField(max_length=380,null=True)
    Image = models.ImageField(upload_to='bookImage/%D/%m/%Y/',null=True)
    BookFile = models.FileField(upload_to='book/%D/%m/%Y/',null=True)

    def __str__(self):
        return self.BookTitle + ' by ' + self.Author



class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE) # this shows the user should only can comment
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete= models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "....  by " + self.user.username
