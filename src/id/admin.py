from django.contrib import admin
from .models import SiteID

# Register your models here.

####### SITE_ID #######
class SiteIDAdmin(admin.ModelAdmin):
    list_display = ['site', 'title','description',]

admin.site.register(SiteID, SiteIDAdmin)
