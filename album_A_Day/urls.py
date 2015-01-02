from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'album_A_Day.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('albumADay.urls')),
    url(r'^(?P<album_id>[0-9]+)/$', 'albumADay.views.detail', name='detail'),
    url(r'^admin/', include(admin.site.urls)),
]
