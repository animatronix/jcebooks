from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^new/$', 'feedbacks.views.feedbackform'),
    (r'^thanks/$', 'django.views.generic.simple.direct_to_template', { 'template': 'feedbacks/thanks.html' }),
)
