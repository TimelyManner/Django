from django.contrib import admin

# Register your models here.

from chat.models import User, Chatroom

admin.site.register(User)
admin.site.register(Chatroom)