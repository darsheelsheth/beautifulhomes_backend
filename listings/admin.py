from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id','title')
    list_filter = ('realtor', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'city', 'state', 'realtor__name')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)