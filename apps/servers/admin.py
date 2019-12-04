from django.contrib import admin

from .models import Server, ServerType


class ServerAdmin(admin.ModelAdmin):
    list_display = ['zcmodel', 'brand', 'zctype', 'modify_time']



class ServerTypeAdmin(admin.ModelAdmin):
    list_display = ['zctype', 'modify_time']

admin.site.register(Server, ServerAdmin)
admin.site.register(ServerType, ServerTypeAdmin)
