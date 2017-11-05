from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    address = models.CharField(max_length=200, verbose_name='Address')
    contact = models.CharField(max_length=200,verbose_name='Contact')

    class Meta:
        ordering=['id']

    def __str__(self):
        return '%s. %s'%(self.id,self.name)

class Author(models.Model):
    GENDER_TYPE = (
        ('F','FEMALE'),
        ('M','MALE'),
    )
    name = models.CharField(max_length=100, verbose_name='Name')
    info = models.CharField(max_length=500, verbose_name='Information')
    gender = models.CharField(max_length=1, choices=GENDER_TYPE, verbose_name='Gender')
    #publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, verbose_name='Publisher')

    class Meta:
        ordering=['id']

    def __str__(self):
        return '%s. %s'%(self.id,self.name)

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    author = models.ForeignKey(Author, verbose_name='Author',on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200, verbose_name='Description')
    pub_date = models.DateField(null=True, verbose_name='Publish Date')
    pub = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, verbose_name='Publisher')
    isbn = models.CharField(max_length=13,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', verbose_name='ISBN')
    icon = models.ImageField(blank=True, verbose_name='Thumbnail', upload_to='images')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Owner')

    # def image_tag(self):
    #     val = format_html('<img src="{}" width="80" height="120"/>'.format(self.icon))
    #     return val
    # image_tag.short_description = 'Thumbnail'


    class Meta:
        ordering = ['id']
        #permissions = (('new_permission','allow to share this book'),)





