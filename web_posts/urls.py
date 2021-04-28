from django.urls import path

#############################
from web_posts.views import news_posts

urlpatterns = [
    path("", news_posts , name="news_posts")
]
