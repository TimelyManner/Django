from django.contrib import admin

# Register your models here.

from chat.models import User, Chatroom

class ChatroomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title_text']}),
        ('Date Information', {'fields': ['created_date'], 'classes':['collapse']}),        
    ]

    list_display = ('title_text', 'created_date' )
    list_filter = ['created_date']
    search_fields = ['title_text']

admin.site.register(User)
admin.site.register(Chatroom, ChatroomAdmin)