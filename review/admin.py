from django.contrib import admin
from .models import Result
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_disply=['title','question']
    list_disply_links=['title','question']
admin.site.register(Result,PostAdmin)