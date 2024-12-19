from django.contrib import admin
from shop.models import *
from django.contrib.contenttypes.admin import GenericStackedInline, GenericTabularInline

class ItemInLine(admin.TabularInline):
    model = Item
    extra = 0



class ImageInline(GenericStackedInline):  
    model = Image
    extra = 0
    fk_name = "content_type"




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    ordering =  ['name']
    inlines = [ItemInLine, ImageInline]

admin.site.register(Category, CategoryAdmin)




class TagInLine(admin. StackedInline):
    model = Tag.items.through
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description']
    search_fields = ['name', 'description']
    ordering =  ['price']
    inlines = [TagInLine, ImageInline]

admin.site.register(Item, ItemAdmin)




class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Tag, ItemAdmin)








