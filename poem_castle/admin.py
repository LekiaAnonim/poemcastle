from django.contrib import admin
from .models import Collection, Poem, Author
# Register your models here.


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    list_display = ('name', 'slug')
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('full_name',)
    list_display = ('full_name',)
    list_filter = ("full_name",)
    search_fields = ("full_name",)

@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'collection', 'featured_image', 'body', 'add_to_featured_poems')
    list_display = ('title', 'collection', 'featured_image', 'add_to_featured_poems')
    list_filter = ("title",)
    search_fields = ("title",)
    prepopulated_fields = {'slug': ('title',)}