from django.conf.urls import url

from . import views

app_name = 'lab'
urlpatterns = [
    # ex: /lab/
    # url(r'^$', views.index, name='index'),
    # ex: /lab/5/
    url(r'^(?P<lab_id>[0-9]+)/$', views.lab_detail, name='lab_detail'),
]
