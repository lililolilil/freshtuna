from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

# Register your models here.
from .models import Post,Board

class PostAdmin(SummernoteModelAdmin):
	pass
class BoardAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Post, PostAdmin)
admin.site.register(Board)