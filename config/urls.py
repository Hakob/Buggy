from django.conf.urls import url, include
from django.contrib import admin

import buggy.urls
import buggy_accounts.urls


urlpatterns = [
    url(r'^', include(buggy.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(buggy_accounts.urls)),
]
