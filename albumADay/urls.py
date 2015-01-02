from django.conf.urls import url

from albumADay import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
