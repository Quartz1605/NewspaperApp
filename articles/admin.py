from django.contrib import admin
from .models import Article,Comment

# Register your models here.

# This stuff here is to display your stuff better on the admin page

#class CommentInline(admin.StackedInline):
  #model = Comment

class CommentInline(admin.TabularInline):
  model = Comment
  extra = 0

#class AdminView(admin.ModelAdmin):
  
  
class ArticleAdmin(admin.ModelAdmin):
  inlines = [
    CommentInline,
  ]

  list_display = [
    "title",
    "body",
    "author",
  ]



admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
