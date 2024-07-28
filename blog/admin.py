from django.contrib import admin
from .models import Post,Category,Comment,Reply

# Register your models here.


admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Comment)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['slug','title']