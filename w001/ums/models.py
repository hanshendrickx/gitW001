"""flexible page"""

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

class UmsPage(Page):
    """Flexible page class"""
    
    template = "ums/ums_page.html"
    
    # to do add streamfields
    # content = Streamfeild()
    
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]
    
    class Meta: 
        verbose_name = "Ums Page"
        verbose_name_plural = "Ums Pages"

