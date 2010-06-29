from django.contrib import admin
from photologue.models import Photo
from models import *

class entryAdmin(admin.ModelAdmin):
    pass
admin.site.register(entry, entryAdmin)

class pageAdmin(admin.ModelAdmin):
    pass
admin.site.register(page, pageAdmin)