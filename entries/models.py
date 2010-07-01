from django.db import models
from django.template.loader import render_to_string
from django.contrib.markup.templatetags.markup import textile
from photologue.models import Photo

class entry(models.Model):
    TYPE_CHOICES = (
        ('leftimage','Standard, image(s) to the left'),
        ('rightimage', 'Standard, image(s) to the right'),
        ('fourcolumn', 'Four colmuns of text only'),
        ('twocolSmallImgs', 'Two columns of text with small images'),
        ('TxtImgTxtImg', 'Four columns A: text, images, text and then images.')
    )
    entryType = models.CharField(max_length=25,choices=TYPE_CHOICES)
    title = models.CharField(max_length=250)
    first_column_text = models.TextField()
    second_column_text = models.TextField(blank=True)
    third_column_text = models.TextField(blank=True)
    fourth_column_text = models.TextField(blank=True)
    first_column_images = models.ManyToManyField(Photo, related_name='entry_first_column_images', blank=True)
    second_column_images = models.ManyToManyField(Photo, related_name='entry_second_colum_images',blank=True)
    def __unicode__(self):
        return self.title
    class Meta: 
        verbose_name =  'Entry' 
        verbose_name_plural = 'Entries'
    def firstText(self):
        return textile(self.first_column_text)
    def secondText(self):
        return textile(self.second_column_text)
    def thirdText(self):
        return textile(self.third_column_text)
    def fourthText(self):
        return textile(self.fourth_column_text)  
    def render(self):
        return render_to_string('entries/{0}.html'.format(self.entryType), {'entry': self})     

