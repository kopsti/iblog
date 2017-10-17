from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.sites.models import Site

class SiteID(models.Model):

    site            = models.OneToOneField(Site, related_name='site_id')
    title           = models.CharField(max_length=100)
    description     = models.CharField(max_length=200, blank=True, null=True)
    logo            = models.ImageField(null=True, blank=True, upload_to='images/site-id')
    favicon         = models.ImageField(null=True, blank=True, upload_to='images/site-id')

    def __str__(self):
        return self.title
