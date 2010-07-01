from django.db import models
from django.template.loader import render_to_string
from feincms.module.page.models import Page
from entries.models import entry


# feinCMS stuff below:

Page.register_templates({
    'title': 'Standard template',
    'path': 'base.html',
    'regions': (
        ('main', 'Main content area'),
        ),
    })
    
class EntryContent(models.Model): 
    """ 
    A single entry from the entries database 
    """ 
    theEntry = models.ForeignKey(entry, verbose_name='Entry')
    class Meta: 
        abstract = True 
        verbose_name = 'Entry' 
        verbose_name_plural = 'Entries'
    def render(self, **kwargs): 
        return self.theEntry.render()

Page.create_content_type(EntryContent)