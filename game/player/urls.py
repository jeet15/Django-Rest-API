from django.conf.urls import patterns,include, url
from django.conf.urls import patterns, url

#from rest_framework.urlpatterns import format_suffix_patterns

from player import views



urlpatterns = [
    url(r'^players/$', views.PlayersList.as_view()),
    url(r'^players/(?P<pk>[0-9]+)/$', views.PlayerDetail.as_view()),

]

#urlpatterns = format_suffix_patterns(urlpatterns)