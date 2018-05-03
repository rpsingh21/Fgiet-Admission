from django.conf.urls import url

from .views import (
    home_view,
    form_view,
    fqs_view,
    success_view,
    application_view
)

urlpatterns = [
    url(r'^$', home_view, name='home'),
    url(r'^form/(?P<year>[\w-]+)/(?P<course>[\w-]+)/$', form_view, name='form'),
    url(r'^success/$',success_view, name='success'),
    url(r'^applicant/(?P<id>\d+)$',application_view, name="application"),
    url(r'^fqs/$',fqs_view,name='fqs')
]