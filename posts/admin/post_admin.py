from django.contrib import admin
from posts.models import Post

# Otra via para registrar el modelo en el admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'post_title',
        'post_content',
        'published_date',
    ]

    list_display_links = [
        'id',
        'post_title',
    ]

    list_filter = [
        'published_date',
    ]

    search_fields = [
        'post_title',
        'post_content',
    ]

# Una via para registrar el modelo en el admin
# admin.site.register(Post, PostAdmin)
