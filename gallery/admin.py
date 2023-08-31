from django.contrib import admin
from .models import Photo, Category
from django.utils.html import format_html


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_images')
    inlines = [PhotoInline]

    def display_images(self, obj):
        images = obj.photo_set.all()  # Retrieve related images for the category
        image_tags = []
        for image in images:
            image_url = image.image.url
            image_tags.append(f'<a href="{image_url}" target="_blank"><img src="{image_url}" width="50" height="50" /></a>')
        return format_html(' '.join(image_tags))

    display_images.allow_tags = True
    display_images.short_description = 'Images'


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'display_category', 'display_image')

    def display_category(self, obj):
        return obj.category.name if obj.category else 'No Category'
    
    display_category.short_description = 'Category'

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return ''
    
    display_image.short_description = 'Image'








admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
