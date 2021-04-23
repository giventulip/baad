from django.shortcuts import render

from navigationbar.models import Navigation
from category.models import CategoryByNav


# Create your views here.
def navbar(request):
    nav_obj = Navigation.objects.all()
    cat_obj = CategoryByNav.objects.all()
    context = {
        "navlist": nav_obj,
        "categorilist": cat_obj
    }
    return render(request, "shared/navbar.html", context)
