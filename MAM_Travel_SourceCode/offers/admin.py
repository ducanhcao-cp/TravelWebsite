from django.contrib import admin
from .models import Tours, tourImages, Deal
# Register your models here.
# admin.site.register(Tours) 
admin.site.register(Deal)

class tourImagesAdmin(admin.StackedInline):
    model = tourImages
 
@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    inlines = [tourImagesAdmin]
 
    class Meta:
       model = Tours
 
@admin.register(tourImages)
class tourImagesAdmin(admin.ModelAdmin):
    pass