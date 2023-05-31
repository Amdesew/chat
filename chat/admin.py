from django.contrib import admin
from .models import Room, Message

class RoomAdmin(admin.ModelAdmin):
    list_display = ('')


# Register your models here.
admin.site.register(Room)
admin.site.register(Message)