from django.conf.urls import url, include
import welcome

urlpatterns = [
    url(r'^view1', welcome.views.view1, name='view1'),
]
