from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, view1, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^landpage/',include('landpage.urls')),
    url(r'^$', index),
    url(r'^$', view1),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
