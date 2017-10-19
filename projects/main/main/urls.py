# Main File of urls
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # first_app is targeting /apps/first_app/urls.py.
    url(r'^', include('apps.first_app.urls')),
    url(r'^first_app/', include('apps.first_app.urls')),
    # This Blogs is targeting /apps/blogs/urls.py.
    url(r'^blogs/', include('apps.blogs.urls')),
    # This is targeting /apps/time_display/urls.py.
    url(r'^time_display/', include('apps.time_display.urls')),
    #This targeting /apps/random_word/urls.py
    url(r'^random_word/', include('apps.random_word.urls')),

    # This is the admin path
    url(r'^admin/', admin.site.urls)
]
