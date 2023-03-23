from django.contrib import admin
from .models import Profile,Info

# Register your models here.
@admin.register(Profile)
class ModelAdmin(admin.ModelAdmin):
    list_display=['id','user','profession','phone_number','activity_status']

@admin.register(Info)
class ModelAdmin(admin.ModelAdmin):
    list_display=['id','profile','consultation_fee','meeting_time','wallet']
