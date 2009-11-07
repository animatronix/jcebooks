from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    url(r'^$', "views.index", name='site_index'),
    url(r'^about', "views.about", name='site_about'),
    url(r'^project', "views.project", name='site_project'),
    url(r'^contact/thanks', "views.contact_thanks", name='site_contact_thanks'),
    url(r'^contact', "feedbacks.views.feedbackform", name='site_contact'),
    url(r'^jci', "views.jci", name='site_jci'),
)

# serve static files in development server
import sys
if 'runserver' in sys.argv:
    media_url = settings.MEDIA_URL
    if media_url.startswith('/'):
        media_url = media_url[1:]
    if media_url.endswith('/'):
        media_url = media_url[:-1]
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,
             'show_indexes': True,
            },
        )
    )
