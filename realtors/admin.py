from django.contrib import admin
from realtors.models import Realtor

class Admin_Realtors(admin.ModelAdmin):
    list_display = ('id','name','phone','email','is_mvp','hire_date')
    list_display_links = ('name','phone','email','hire_date')
    search_fields = ('name',)
    list_filter =  ('name',)
    list_editable = ('is_mvp',)
    list_per_page = 30



admin.site.register(Realtor , Admin_Realtors)
