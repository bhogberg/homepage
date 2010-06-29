from django.db import models
from django.template.loader import render_to_string
from photologue.models import Photo, PhotoSize

class entry(models.Model):
    TYPE_CHOICES = (
        ('leftimage','Standard, image(s) to the left'),
        ('rightimage', 'Standard, image(s) to the right'),
        ('fourcolumn', 'Four colmuns of text'),
        ('twocolSmallImgs', 'Two columns of text with small images')
    )
    entryType = models.CharField(max_length=25,choices=TYPE_CHOICES)
    title = models.CharField(max_length=250)
    first_column_text = models.TextField()
    second_column_text = models.TextField(blank=True)
    third_column_text = models.TextField(blank=True)
    fourth_column_text = models.TextField(blank=True)
    img_size = models.ForeignKey(PhotoSize, verbose_name='Size of images') 
    first_column_images = models.ManyToManyField(Photo, related_name='entry_first_column_images')
    second_column_images = models.ManyToManyField(Photo, related_name='entry_second_colum_images',blank=True)
    def __unicode__(self):
        return self.title
    class Meta: 
        verbose_name =  'Entry' 
        verbose_name_plural = 'Entries'
    def render(self):
        return render_to_string('pages/entry/%s.html' %s self.entryType, {'entry': self,})     



class page(models.Model):
    title = models.CharField(max_length = 60)
    slug = models.CharField(max_length = 40)
    content_regions = models.ManyToManyField(entry)
    