from django.db import models
from django.template.loader import render_to_string
from django.http import HttpResponse
from feincms.module.page.models import Page
from entries.models import entry
from publications.models import publication


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
  
class PublicationList(models.Model):
    """ 
    A simple publication list that display all publications.
    """
    selected_publications = models.ManyToManyField(publication)
    class Meta: 
        abstract = True 
        verbose_name = 'Publication List' 
        verbose_name_plural = 'Publication Lists'
    def render(self, **kwargs):
        return render_to_string('publications/publication_list.html', {'publication_list': self.selected_publications})

Page.create_content_type(EntryContent)
Page.create_content_type(PublicationList)