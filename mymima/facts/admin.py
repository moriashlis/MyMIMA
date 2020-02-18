from django.contrib import admin

# Register your models here.
from facts import models
from django.contrib import admin



class SongAdmin(admin.ModelAdmin):

    # search_fields = (
    #     'id',
    #     'title',
    #     'amount',
    #     'description',
    # )
    list_display = (
        'id',
        'name',
        'artist',


    )
    list_filter = (
        'artist',
    )

admin.site.register(models.Artist)
admin.site.register(models.Song,SongAdmin)
admin.site.register(models.Facts)
