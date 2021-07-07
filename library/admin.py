from django.contrib import admin

from .models import Author, Publisher, Book, Store

@admin.register
class BookInline(admin.TabularInline):
    model = Book

с

# Register your models here.
