from django.contrib import admin

from book.models import Book

from book.models import Book, Reviews, Tag, Category

admin.site.register(Book)
admin.site.register(Reviews)
admin.site.register(Tag)
admin.site.register(Category)
