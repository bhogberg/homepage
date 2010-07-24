from django.contrib import admin
from models import *

class publicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(publication, publicationAdmin)
