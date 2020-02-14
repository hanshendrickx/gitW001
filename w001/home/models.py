from django.db import models
 
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
 
class HomePage(Page):
    """Home page model."""
 
    template = "home/home_page.html"
    max_count = 1
 
    banner_title = models.CharField(max_length=100, blank=False, null=True)
 
    content_panels = Page.content_panels + [
        FieldPanel("banner_title")
    ]
 	
    api_fields = [
        APIField("banner_title"),
    ]
    
    class Meta:
 
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
    
