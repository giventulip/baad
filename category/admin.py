from django.contrib import admin

# Register your models here.
from category.models import CategoryByNav

class ModelCategory(admin.ModelAdmin):
    list_display = ["__str__", "title", "link", "id"]

    class Meta:
        model = CategoryByNav


admin.site.register(CategoryByNav, ModelCategory)