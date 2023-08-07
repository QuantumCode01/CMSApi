from django.contrib import admin
from .models import Post,like
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display=['id', 'title','description', 'content','creation_date','name']
 
@admin.register(like)
class likeAdmin(admin.ModelAdmin):
 list_display=['id','post_id','user_id']
 

