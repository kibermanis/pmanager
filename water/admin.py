from django.contrib import admin

from .models import BuildingCategory, ApartmentCategory, WaterCounterCategory, WaterCounterReadings

# class ListingApartmentCategory(admin.ModelAdmin):
#     list_display = ('apartment_num', 'apartment_owner')
#
# class ListingWaterCounterCategory(admin.ModelAdmin):
#     list_display = ('water_counter_num', 'water_counter_type', 'apartment_num')
#     list_filter = ('apartment_num',)

admin.site.register(BuildingCategory)
admin.site.register(ApartmentCategory)
# admin.site.register(ListingApartmentCategory)
# admin.site.register(ListingWaterCounterCategory)
admin.site.register(WaterCounterCategory)
admin.site.register(WaterCounterReadings)

