from django.conf.urls import url

from . import views

app_name = 'lexicon'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<entry_id>[0-9]+)/$', views.entry_detail, name='entry_detail'),
]
