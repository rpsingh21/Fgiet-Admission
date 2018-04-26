from django.conf.urls import url

from .views import formView

urlpatterns = [
    url(r'^$', formView, name='form')
]