from django.contrib import admin
from .models import Cat


# Register your models here.
class CatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cat, CatAdmin)
