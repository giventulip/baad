from django.shortcuts import render

# Create your views here.
def news_posts(request):
    context = {}
    return render(request, "listview.html", context)
