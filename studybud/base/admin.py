from django.contrib import admin
from .models import Room, Topic, Messages, User


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'created')


admin.site.register(User)
admin.site.register(Room, RoomAdmin)
admin.site.register(Topic)
admin.site.register(Messages, MessagesAdmin)
