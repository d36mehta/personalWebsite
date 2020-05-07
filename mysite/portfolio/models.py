import os

from django.db import models


# Create your models here.
class TextBubble(models.Model):
    TAG = (
        ('P', 'Project'),
        ('E', 'Experience'),
        ('I', 'Blog'),
    )
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=1, choices=TAG)
    pub_date = models.DateTimeField('date_published')
    text = models.TextField()
    picture = models.ImageField(upload_to='images/')
    links = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    pdf_link = models.FileField(upload_to='uploads/', max_length=100)
    pdf_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pdf_name


class Quotes(models.Model):
    quote = models.CharField(max_length=800)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.quote


class Languages(models.Model):
    language_link = models.ForeignKey(TextBubble, on_delete=models.CASCADE, related_name='llink')
    languages = models.CharField(max_length=100, blank=True)
