from django.contrib import admin
from .models import DeviceModel, Color, Capacity, CPU, Out_Camera, Authentication

admin.site.register(DeviceModel)


@admin.register(Capacity)
class CapacityAdmin(admin.ModelAdmin):
    list_display = ('capacities',)
    list_display_links = ('capacities',)


admin.site.register(Color)


admin.site.register(CPU)
admin.site.register(Out_Camera)
admin.site.register(Authentication)
