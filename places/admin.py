from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Place, Image

from adminsortable2.admin import SortableAdminMixin, SortableTabularInline


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['image', 'get_preview', 'position']
    extra = 0
    
    def get_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
