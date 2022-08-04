from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost

# Apply summernote to all TextField in model.
class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ['slug']
    list_display = ('id','title', 'category', 'date_created')
    list_display_links = ('id', 'title')
    list_per_page = 25
    summernote_fields = ('content')

admin.site.register(BlogPost, BlogPostAdmin)
