from django.contrib import admin
from models import *

# Register your models here.
class QuoteInlineAdmin(admin.TabularInline):
    model = Quote

class LocationInlineAdmin(admin.TabularInline):
    model = Location

class BookAdmin(admin.ModelAdmin):
    inlines = [LocationInlineAdmin, QuoteInlineAdmin]

admin.site.register(Book, BookAdmin)
admin.site.register(Quote)
admin.site.register(Location)
