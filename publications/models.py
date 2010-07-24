from django.db import models
from photologue.models import Photo
from django.template.loader import render_to_string

# Create your models here.

class publication(models.Model):
    TYPE_CHOICES = (
        ('article','Journal article'),
        ('proceeding', 'Conference contribution'),
        ('book', 'Book or thesis, PhD and other'),
        ('patent', 'Patent'),
        ('bookChapter', 'Book chapter'),
    )
    publication_type = models.CharField(max_length=25,choices=TYPE_CHOICES)
    title = models.CharField(max_length=250)
    date_published = models.DateField()
    authors = models.CharField(max_length=250)
    journal = models.CharField(max_length=250, blank=True)
    pages = models.CharField(max_length=30, blank=True)
    volume = models.CharField(max_length=30, blank=True)
    book_or_patent_info = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    #pdf_file = models.ForeignKey(FileUpload, related_name='Publication_pdf', blank=True)
    pdf_file = models.FileField('fileEEE', upload_to='publications')
    publication_image = models.ForeignKey(Photo, related_name='Publication_Image', blank=True)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-date_published']
        verbose_name_plural = 'Publications'
    def render(self):
        return render_to_string('publications/publication.html', {'publication': self})