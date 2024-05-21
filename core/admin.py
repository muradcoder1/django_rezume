from django.contrib import admin
from .models import GeneralSetting,ImageSetting,About,Skills
# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','paramater','created_date','updated_date']
    list_editable=['name','paramater']
    list_filter=['name']

    class Meta:
        verbose = GeneralSetting

@admin.register(ImageSetting)
class ImageSettingsAdmin(admin.ModelAdmin):
    list_display=["id","name","description","file"]
    class Meta:
        verbose = GeneralSetting
@admin.register(About)
class Aboutadmin(admin.ModelAdmin):
    list_display = ['id','name','description','text','created_date','updated_date']
    list_editable=['name','text']
    list_filter=['name']
    class Meta:

        verbose = About
@admin.register(Skills)
class Skills(admin.ModelAdmin):
    
    list_display = ['id','order','name','percentage']
    list_editable=['name','percentage']
    class Meta:
        verbose=Skills

