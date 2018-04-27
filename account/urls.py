from django.conf.urls import url

from .views import adminTableView

urlpatterns = [
    url(r'^$', adminTableView, name='table')
]
