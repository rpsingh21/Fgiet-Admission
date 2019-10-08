from django.conf.urls import url

from .views import adminTableView, login_view, logout_view

urlpatterns = [
    url(r'^$', adminTableView, name='table'),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout")
]
