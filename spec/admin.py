from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Activity;



class SpecAdmin(admin.ModelAdmin):
    search_fields = ['subject'];

admin.site.register(Activity, SpecAdmin);


