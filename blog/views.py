from django.shortcuts import render
from datetime import date

all_posts=[
    {
    "slug":"hike-in-the-mountains",
    "image":"surya.JPG",
    "author":"vasudev gitesh",
    "date":date(2025,4,13),
    "title":"Mountain Hiking",
    "excerpt":"there's nothing like the views it provides",
    "content":"covered devkund,kalu,harischandragad,aadrai,lohagad,andarbaan and it was a unreal experience"
    },
    {
    "slug":"us-citizen",
    "image":"yeshu.JPG",
    "author":"yeshwanth chandrasekhar",
    "date":date(2025,4,17),
    "title":"Mountain Hiking",
    "excerpt":"better than chicaGO",
    "content":"covered devkund,kalu,harischandragad,aadrai,lohagad,andarbaan and it was a unreal experience"
    },
   
    {
    "slug":"ballari-hikes",
    "image":"sai.JPG",
    "author":"ballari bros",
    "date":date(2025,5,12),
    "title":"bhavya sai",
    "excerpt":"sai loda the king",
    "content":"covered devkund,kalu,harischandragad,aadrai,lohagad,andarbaan and it was a unreal experience"
    },
    {
    "slug":"pulicallu",
    "image":"DJI_20240830162215_0139_D.JPG",
    "author":"greeshmonth",
    "date":date(2025,1,1),
    "title":"geechu",
    "excerpt":"my first vlog",
    "content":"covered australia and paris so far"
    },
    {
    "slug":"noothan",
    "image":"DSC_5540.JPG",
    "author":"noothan prasad",
    "date":date(2025,1,1),
    "title":"maraige",
    "excerpt":"marriage celebration",
    "content":"bengaluru boys"
    }
]
    
def get_date(post):
    return post['date']

# Create your views here.
def startingpage(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request, "blog/index.html",{
        "posts":latest_posts
    })


def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts
    })


def post_details(request, slug):
    identified_post=next(post for post in all_posts if post['slug']==slug)
    return render(request,"blog/post-detail.html",{
        "post":identified_post
    })
