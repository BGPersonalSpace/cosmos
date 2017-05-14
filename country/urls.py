from django.conf.urls import url

from . import views
from lab import views as lab_views

app_name = 'country'
urlpatterns = [
    # ex: /country/
    # url(r'^$', views.index, name='index'),
    # ex: /country/5/
    url(r'^$', views.countries, name='countries'),
    url(r'^(?P<country_id>[0-9]+)/$', views.country_detail, name='country_detail'),
    url(r'^list/$', views.countries, name='countries'),
    url(r'^(?P<country_id>[0-9]+)/labs/$', lab_views.labs_by_country, name='labs_by_country'),
    url(r'^(?P<country_id>[0-9]+)/tests/$', lab_views.tests_by_country, name='tests_by_country'),
]
