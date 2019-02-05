from django.contrib import admin

# Register your models here.

from chat import models
'''
class ChatroomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title_text', 'users', 'owner']}),
        ('Date Information', {'fields': ['created_date'], 'classes':['collapse']}),        
    ]

    list_display = ('title_text', 'created_date', 'users', 'owner' )
    list_filter = ['created_date']
    search_fields = ['title_text']
'''
admin.site.register(models.User)
admin.site.register(models.Chatroom)