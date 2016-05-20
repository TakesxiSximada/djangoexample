from django.conf.urls import url, include

import rest_framework_swagger.urls

from .users import urls as users_urls
from .accounts import urls as accounts_urls
from .organizations import urls as organizations_urls


urlpatterns_v1 = [
    url('^users/', include(users_urls)),
    url('^organizations/', include(organizations_urls)),
    url('^accounts/', include(accounts_urls)),
]


urlpatterns_v2 = [
]


urlpatterns = [
    url('^docs/', include(rest_framework_swagger.urls)),
    url('^v1/', include(urlpatterns_v1)),
    url('^v2/', include(urlpatterns_v2)),
]
