from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from blog.models import Post,BookSection,Topic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout
# Create your views here.

### html pages
def topic_page(request,rewrite_topicsub):# filter(Topic__topicsub__contains=subtopic)  get(topicsub__contains=subtopic)
    # alpha = subtopic
    all_Post = Post.objects.filter(rewrite_topicsub__icontains=rewrite_topicsub)
    context = {'all_Post': all_Post,
                'rewrite_topicsub':rewrite_topicsub.replace('_',' '),
         }
    return render(request,'home/sub.html' , context)
# 
def home(request):
    all_post = Post.objects.all()
    subtopicsLis = set()
    for post in all_post:
        subtop = post.rewrite_topicsub
        p = subtopicsLis.add(subtop)
    subtopicsLis1 = list(subtopicsLis)
    context = { "subtopicsLis1": subtopicsLis1,
                "all_post" : all_post,
                "home_page": "active",
                }   
    return render(request, 'home/Home.html',context)

def archive(request):
    all_post = Post.objects.all()
    y = {"JAN":1 , "FEB" :2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8, "SEPT":9,'OCT':10,'NOV':11,'DEC':12}

    dic = {}
    for post in all_post:
        monthPosted = post.monthly
        yearPosted = post.yearly
        if yearPosted in dic:
            if monthPosted not in dic[yearPosted]:
                dic[yearPosted].append(monthPosted)
                if len(dic[yearPosted]) > 1:
                    B = sorted(dic[yearPosted] , key= lambda x: y.get(x))
                    dic[yearPosted] = B
        else:
            dic[yearPosted] = [monthPosted]
    print(dic)
    
    context = {"archive_page": "active",
                "dic" : dic}
    return render(request,'home/archive.html',context)

def archive_page(request,year,month):
    all_Post = Post.objects.filter(yearly__icontains=year).filter(monthly__icontains=month)

    context = {'all_Post': all_Post,'archive_page':'active','year':year,'month':month}
    return render(request,'home/archive_page.html',context)

def about(request):
    context = {"about_page":"active"}
    return render(request, 'home/about.html',context)

def books(request):
    all_books = BookSection.objects.all()
    context = {"books_page":"active",
                "all_books": all_books ,
    }
    return render(request, 'home/books.html',context)

def contact(request):
    context = {"contact_page":"active"}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<4:
            messages.error(request,"Please fill the form correctly ")
        else:
            contac = Contact(name= name, email=email, phone=phone, content=content)
            contac.save()
            messages.success(request, 'your form is successfully sent ')


    return render(request, 'home/contact.html',context)



def search(request):
    query = request.GET['query']
    if len(query) > 80:
        all_Post = []
    else:
        all_Post = Post.objects.filter(title__icontains=query)
    context = {'all_Post': all_Post , 'query': query }
    return render(request,'home/search.html' , context)


def joinus(request):
    return render(request,'home/joinus.html' )


### Authentication apis
def handleSignup(request):

    if request.method == 'POST':
        usernae = request.POST['username']  # request.POST is a dictionary where we take the value of username
        email = request.POST['email1']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(usernae)>20:
            messages.error(request,"Username must be under 20 characters")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request,"password do not match")
            return redirect('home')
        if not usernae.isalnum():
            messages.error(request, "Username must contain only letters and numbers")
            return redirect('home')



        myuser = User.objects.create_user(usernae, email, pass1 )
        myuser.save()
        messages.success(request,f'Your account is successfully created {request.user}')
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']  # request.POST is a dictionary where we take the value of username
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In ")
            return redirect('home')
        else:
            messages.error(request, "INVALID CREDENTIALS : Please try again")
    return redirect('home')   


def handleLogout(request):
    
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Successfully Logged Out')
        return redirect('home')
    else:
        messages.info(request,"Please login !")
        return redirect('home')

