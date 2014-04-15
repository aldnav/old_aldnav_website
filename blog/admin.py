from django.contrib import admin
from blog.models import Post, Tag

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title','body']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
        
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)