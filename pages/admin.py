from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact,Post
# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email',)
    list_display_links = ('id', 'name')  
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published',)
    list_display_links = ('id', 'title')
    list_editable = ('is_published',) 
    search_fields = ('title',)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Post,PostAdmin)