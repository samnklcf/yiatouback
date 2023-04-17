from django.contrib import admin
from .models import *

# Register your models here

class ListeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'Prix')

admin.site.register(Liste, ListeAdmin)
admin.site.register(CleApi)
