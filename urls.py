from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

import os.path


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/(.*)', admin.site.root),
    (r'^photologue/', include('photologue.urls')),
    (r'^pages/$', 'views.entries_index'),
    
    # Need to delete when going to production:
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'media')}),
)
