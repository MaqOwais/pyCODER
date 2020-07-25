"""pyCODER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.contrib import admin
from django.urls import path , include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from blog.feeds import LatestPostsFeed
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "SHO-ADMIN"
admin.site.site_title = "SHO-ADMIN_PANEL"
admin.site.index_title = "WELCOME TO SHO-ADMIN_PANEL"

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('maqoAdmin786/', admin.site.urls),
    path('blog/',include('blog.url')),
    path('',include('home.urlh')),
    path('summernote/', include('django_summernote.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('feed/rss', LatestPostsFeed(), name='post_feed'),
] 
# + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)