from django.conf.urls import url
from Site.core import views

urlpatterns = [
    url(r'^$', views.Home, name='Home'),
    url('update/(?P<pk>.+)$', views.update, name='url_update'),
]