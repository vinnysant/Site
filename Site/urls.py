from django.conf.urls import url, include

urlpatterns = [
    url(r'^site/', include('Site.core.urls')),
]