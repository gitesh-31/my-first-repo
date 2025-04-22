from django.urls import path
from . import views


urlpatterns = [
    path("",views.startingpage,name="starting-page"),                                 #homepage
    path("posts",views.posts,name="posts-page"),                            #to view all posts
    path("posts/<slug:slug>",views.post_details,name="post-detail-page")                 # to view individual posts
]
