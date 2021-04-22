from django.shortcuts import render

from navigationbar.models import Navigation


# Create your views here.
def navbar(request):
    nav_obj = Navigation.objects.all()
    context = {
        "navlist": nav_obj
    }
    return render(request, "shared/navbar.html", context)
