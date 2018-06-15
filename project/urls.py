from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from welcome.views import index, view1

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    url(r'^view1.html', view1, name='view1'),
    url(r'^', include('personal.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^pages/', include('welcome.urls')),    
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


