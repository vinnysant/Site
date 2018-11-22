from django.conf.urls import url
from Site.core import views

urlpatterns = [
    url(r'^$', views.Home, name='Home'),

]