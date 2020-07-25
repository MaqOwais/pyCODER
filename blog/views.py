from django.shortcuts import render , HttpResponse, redirect
from .models import Post, BlogComment
from django.contrib import messages
from .templatetags import extras
from django.http import request
from tracking_analyzer.models import Tracker
from django.contrib.auth.decorators import login_required

# Create your views here.

def blogHome(request):
    all_post = Post.objects.all()
    context = {"all_post": all_post ,
                "blog_page": "active"}
    return render(request , 'blog/blogHome.html', context)

# @login_required
def blogPost(request,slug):

    post = Post.objects.filter(slug=slug).first()       # once go through filter() while reformating and further understanding...
    # postcont = post.content
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {"post":post ,
               "blog_post": "active",
               "comments" : comments,
               "user" : request.user,
               "replyDict" : replyDict,
    }
    # Tracker.objects.create_from_request(request, post) # uncommon out while deployment

    return render(request ,'blog/blogPost.html',context)

@login_required
def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == None:
            comment = BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,"Your comment has been posted  successfully")

        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment,user=user,post=post, parent=parent)
            comment.save()
            messages.success(request,"Your reply has been posted successfully")

    return redirect(f"/blog/{post.slug}")
