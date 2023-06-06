from django.shortcuts import render,redirect
from matplotlib.pyplot import title
from DB.models import Comment, New,Blog
from Sports.data import data,ref_time,categories
from django.core.paginator import Paginator
import random
from .forms import MyForm

def index(request):
    #---------------------Refreshing------------------
    # for i in ["All Headlines","Top Headlines","Olympics",
    # "Soccer","MLB",'NHL','NBA','NFL',"College Football",
    # "USFL","College Basketball","NASCAR","Motor Sports",
    # "UFC","Golf","Tennis","Horseracing","WNBA","Women College Basketball"]:
        # if ref_time(i): #True if more than 59 minutes has passed for last data fetch
        # data(i)
    #---------------------Obtaining-------------------
    all_headlines = New.objects.filter(our_category="All Headlines")
    top_headlines = New.objects.filter(our_category="Top Headlines")
    olympics = New.objects.filter(our_category="Olympics")
    soccer = New.objects.filter(our_category="Soccer")
    mlb = New.objects.filter(our_category="MLB")
    nba = New.objects.filter(our_category="NBA")
    nhl = New.objects.filter(our_category="NHL")
    #---------------------Returnig------------------
    return render(request,'index.html',{
        "five_all_headlines":all_headlines[0:5],
        "trending_top":top_headlines[0],
        "trending_bottom":top_headlines[1:4],
        "riht_content":top_headlines[4:8],
        "olympics":olympics[0:8],
        "soccer":soccer[0:8],
        "nba":nba[0:8],
        "nhl":nhl[0:8],
        "mlb":mlb[0:4],
        "categories":categories[8::],
        "categories2":categories[0:8],
        "title":"Sports"
        })

def category(request,id,idd):
    #------------------------Refreshing--------------------
    # if ref_time(id):
    #     data(id)
    #------------------------Obtaining--------------------
    objs = New.objects.filter(our_category=id).order_by('rank')
    paginated = Paginator(objs,per_page=20)
    page1 = paginated.page(idd)
    objs = page1.object_list
    no_of_pages = paginated.num_pages
    pages = [i for i in range(1,no_of_pages+1)]
    #-----------------------Returning-------------------
    return render(request,'category.html',{
        "categories":categories[8::],
        "categories2":categories[0:8],
        "category":id,
        "objects":objs,
        "no_of_pages":pages,
        "title":id,
        })

def category2(request,id):
    #------------------------Refreshing--------------------
    # if ref_time(id):
    #     data(id)
    #------------------------Obtaining--------------------
    objs = New.objects.filter(our_category=id).order_by('rank')
    paginated = Paginator(objs,per_page=20)
    page1 = paginated.page(1)
    objs = page1.object_list
    no_of_pages = paginated.num_pages
    pages = [i for i in range(1,no_of_pages+1)]
    #-----------------------Returning-------------------
    return render(request,'category.html',{
        "categories":categories[8::],
        "categories2":categories[0:8],
        "category":id,
        "objects":objs,
        "no_of_pages":pages,
        "title":id
        })

def blog(request,id):
    #-----------------------Obtaining---------------------
    try:
        obj = Blog.objects.get(blog_url=id)
    except:
        obj = Blog.objects.last()
    all_headlines = New.objects.filter(our_category="All Headlines")
    cat = random.choices(categories,k=8)
    #-----------------------Nvigation on posts---------------
    default = {
            "title":"No more posts",
            "blog_url":obj.blog_url,
            "thumbnail":obj.thumbnail
        }
    list_all_posts = next_post = Blog.objects.filter(our_category=obj.our_category)
    try:
        next_post = list_all_posts.get(id=(obj.id)+1)
    except:
        next_post = default
    try:
        previous_post = list_all_posts.get(id=(obj.id)-1)
    except:
        previous_post = default
    #------------------------Form-------------------------
    #----------Recieving
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    form = MyForm()
    #---------Displaying
    # try:
    comments = Comment.objects.all().order_by('-id')
    comments = comments[0:5]
    # except:
    #     comments = [{'profile_picture':"/media/comments/err.jpg",'text':"Excellent website with good presentation.",'name':"Khalid Ali",'email':"123@456.com",'website':'https://www.hi-goo.com'}]
    #------------------------Returning----------------------
    return render(request,'single-blog.html',{
        "object":obj,
        "recent_posts":all_headlines[0:5],
        "category":cat,
        "categories":categories[8::],
        "categories2":categories[0:8],
        "next_post":next_post,
        "previous_post":previous_post,
        "form":form,
        "comments":comments,
        "title":obj.title
    })

def search(request):

    q = request.GET.get('search')
    objs = Blog.objects.filter(title__icontains=q)
    objs2 = Blog.objects.filter(our_category__icontains=q)
    return render(request,'search.html',{"search1":objs,"search2":objs2})


