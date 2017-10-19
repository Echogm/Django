# urls of random_word app
from django.conf.urls import url
from . import views
urlpatterns = [
    # main url
    url(r'^$', views.index),
    # Generate request route
    url(r'^random/$', views.random),
    # Reset request route
    url(r'^reset/$', views.reset)
]
