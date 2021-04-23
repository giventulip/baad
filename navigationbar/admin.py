from django.contrib import admin

# Register your models here.
from navigationbar.models import Navigation

class ModelNavigations(admin.ModelAdmin):
    list_display = ["__str__", "title", "icon", "link", "on_categorys", "new", "id"]

    class Meta:
        model = Navigation


admin.site.register(Navigation, ModelNavigations)