from django.contrib import admin
from .models import News, Users


# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'text')
    list_display_links = ('date', 'title')
    search_fields = ('date', 'title')
    list_editable = ('text',)
    list_filter = ('title',)


admin.site.register(News)
admin.site.register(Users)
