from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(SummernoteModelAdmin):
	pass

admin.site.register(Post, PostAdmin)
