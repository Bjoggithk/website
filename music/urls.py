from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_View(), name='index'),

    # /music/712/  (talan er id á albúminu)
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_View(), name='detail'),
]
