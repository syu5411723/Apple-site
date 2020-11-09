from django.contrib import admin
from .models import Device, Color, Capacity, CPU, Out_Camera, Authentication

admin.site.register(Device)


@admin.register(Capacity)
class CapacityAdmin(admin.ModelAdmin):
    list_display = ('capacities',)
    list_display_links = ('capacities',)


admin.site.register(Color)

filter_horizontal = ('',)


admin.site.register(CPU)
admin.site.register(Out_Camera)
admin.site.register(Authentication)
