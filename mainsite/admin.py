from django.contrib import admin
from mainsite.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display= ('id','title','slug','pub_date')
    ordering=('-id',)
admin.site.register(Post,PostAdmin)