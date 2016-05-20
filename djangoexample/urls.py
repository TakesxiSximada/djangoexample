from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse

from . import apiurls


def ping(request):
    """for internal health check"""
    return HttpResponse("pong")


urlpatterns = [
    url(r'^ping/', ping),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apiurls))
]
