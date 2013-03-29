from django.conf.urls.defaults import *

urlpatterns = patterns('study_helper.views',
    url(r'^$', 'art', name='home'),
    url(r'^(\d{1})', 'unit', name='unit'),
    url(r'^artist/', 'artist', name='artist'),
    url(r'^category/', 'category', name='category'),
    url(r'^timeline/', 'timeline', name='timeline'),
)