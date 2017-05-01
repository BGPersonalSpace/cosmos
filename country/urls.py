from django.conf.urls import url

from . import views

app_name = 'country'
urlpatterns = [
    # ex: /country/
    # url(r'^$', views.index, name='index'),
    # ex: /country/5/
    url(r'^(?P<country_id>[0-9]+)/$', views.summary, name='summary'),
]
