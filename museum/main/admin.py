from django.contrib import admin

from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'years_of_life', 'exhibition')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'exhibition')
    list_filter = ('name', 'exhibition')
    list_per_page = 13
    # save_on_top = True


class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Association)
admin.site.register(Education)
admin.site.register(Institution)
admin.site.register(ExhibitionPhoto)

admin.site.site_title = "Государственный музей искусств Республики Каракалпакстан имени И.В. Савицкого"
admin.site.site_header = 'Государственный музей искусств Республики Каракалпакстан имени И.В. Савицкого'
