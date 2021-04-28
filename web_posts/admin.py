from django.contrib import admin

# Register your models here.
from web_posts.models import  PostNews, ImageNews

admin.site.register(PostNews)
admin.site.register(ImageNews)