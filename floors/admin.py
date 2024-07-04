from django.contrib import admin

from .models import Floors
from .models import Rows

class FloorAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name',)
    list_display = ('name', 'created_at', 'updated_at')
    ordering = ('created_at',)

class RowsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('name', 'floor', 'orientation')
    list_filter = ('floor',)
    list_display = ('name', 'floor', 'orientation',)
    # fields = ('name', 'floor')
    ordering = ('-created_at',)
    
    # def save_model(self, request, obj, form, change):
    #     if not obj.floor_id:
    #         obj.user_id = request.user.id
    #     obj.save()

admin.site.register(Floors, FloorAdmin)
admin.site.register(Rows, RowsAdmin)