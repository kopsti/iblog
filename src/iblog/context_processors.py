from django.conf import settings
from django.contrib.sites.models import Site
from id.models import SiteID

def current_site(request):
    try:
        current_site = Site.objects.get_current()
        site_title = Site.objects.get_current().site_id.title
        site_description = Site.objects.get_current().site_id.description
        site_logo = Site.objects.get_current().site_id.logo
        site_favicon = Site.objects.get_current().site_id.favicon
        return {
            'current_site': current_site,
            'site_title': site_title,
            'site_description': site_description,
            'site_logo': site_logo,
            'site_favicon': site_favicon,
        }
    except:
        # always return a dict, no matter what!
        return {'current_site':''} # an empty string    
