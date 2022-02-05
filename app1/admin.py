from django.contrib import admin

from .models import Category, Bookmarks

admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bookmarks)


class BookmarksAdmin(admin.ModelAdmin):
    pass
