from django.contrib import admin
from .models import Post,Category,Tag
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'create_time')
    fields = ('name', 'status', 'is_nav')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'create_time')
    fields = ('name', 'status')
