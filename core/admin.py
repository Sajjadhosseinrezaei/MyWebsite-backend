from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Profile, Skill, Technology,
    ProjectCategory, Project, ProjectImage
)

# ========== Profile ==========
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']
    search_fields = ['name', 'email', 'title']


# ========== Skill ==========
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'is_featured', 'icon_preview']
    list_filter = ['is_featured']
    search_fields = ['name', 'description']

    def icon_preview(self, obj):
        if obj.icon_class:
            return format_html(f'<i class="{obj.icon_class}"></i>')
        elif obj.icon_image:
            return format_html(f'<img src="{obj.icon_image.url}" width="24" height="24" />')
        return "-"
    icon_preview.short_description = "آیکن"


# ========== Technology ==========
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon_display', 'color_display']
    search_fields = ['name']

    def icon_display(self, obj):
        if obj.icon:
            return format_html(f'<i class="{obj.icon}"></i>')
        elif obj.icon_image:
            return format_html(f'<img src="{obj.icon_image.url}" width="24" height="24" />')
        return "-"
    icon_display.short_description = 'آیکن'

    def color_display(self, obj):
        if obj.color:
            return format_html(f'<span style="display:inline-block;width:20px;height:20px;background-color:{obj.color};border-radius:50%;"></span> {obj.color}')
        return "-"
    color_display.short_description = 'رنگ'


# ========== ProjectCategory ==========
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


# ========== ProjectImage Inline ==========
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


# ========== Project ==========
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'is_featured', 'order']
    list_filter = ['status', 'is_featured', 'category']
    search_fields = ['title', 'description', 'short_description']
    filter_horizontal = ['technologies']
    inlines = [ProjectImageInline]
    ordering = ['-is_featured', 'order']


# ========== ProjectImage (Optional standalone admin) ==========
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption', 'order']
    search_fields = ['caption', 'project__title']
    ordering = ['order']
