from django.conf.urls import patterns, url

urlpatterns = patterns('vehicles.views',
   url('ajax/lookupVsn/', 'lookupVsn'),
   url(r'^$', 'index'))
   

