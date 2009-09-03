from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import *

from feedbacks.models import Feedback, FeedbackForm

def feedbackform(request):
    if request.method == 'POST': # If the form has been submitted...
        instance = Feedback(text='text', name='name')
        form = FeedbackForm(request.POST, instance=instance) # A form bound to the POST data
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/contact/thanks/') # Redirect after POST
    else:
        form = FeedbackForm()
    
    return render_to_response('contact.html', {'form': form,}, context_instance=RequestContext(request))
