from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.timeStamp

# for getting more delve into this section -->https://www.youtube.com/watch?v=U1f4QTyJBTs