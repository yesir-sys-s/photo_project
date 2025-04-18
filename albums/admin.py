from django.contrib import admin
from django.utils.html import mark_safe
from .models import Album, Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'created_by')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('album', 'caption', 'uploaded_at', 'image_preview')
    search_fields = ('caption', 'album__title')
    list_filter = ('uploaded_at', 'album')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" />')
        return "No image"
    image_preview.short_description = 'Preview'
