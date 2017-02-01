from django.contrib import admin
from blog import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {"slug" : ("title",)}

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
