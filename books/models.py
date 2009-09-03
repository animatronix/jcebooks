import datetime
from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from django.utils.translation import ugettext_lazy as _

class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    logo_image = models.ImageField(upload_to="book_logos/%Y/%m/%d", blank=True)
    source = models.FileField(upload_to="book_files/%Y/%m/%d", blank=True)
    create_date = models.DateTimeField('create date', default=datetime.datetime.now())
    tags = TagField()
    download_count = models.PositiveIntegerField('download_count', default=0)
    creator = creator = models.ForeignKey(User, related_name="created_events", verbose_name=_('creator'))
    ISBN_number = models.CharField(max_length=20, null=True, blank=True)
    author = models.ForeignKey(Author)
