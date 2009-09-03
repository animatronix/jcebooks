from django.db import models
from django.forms import ModelForm
import datetime

class Feedback(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=30, blank=True)
    create_date = models.DateTimeField('create_date', default=datetime.datetime.now())
    ip_address = models.CharField(max_length=15, blank=True, default="none")
    
class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'name']


