from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', views.book, name="single_book"),
    url(r'^author/(?P<id>[0-9]+)/$' , views.author_detail , name="single_author"),
    url(r'^author/$', views.author , name="author"),
    url(r'^$', views.index, name="index"),

]