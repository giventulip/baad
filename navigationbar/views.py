from django.shortcuts import render

# Create your views here.
def navbar(request):
    context = {
        "text" : "Hello World"
    }
    return render(request,"shared/navbar.html", context)
