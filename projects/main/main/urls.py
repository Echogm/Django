"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # first_app is targeting /apps/first_app/urls.py
    url(r'^$', include('apps.first_app.urls')),
    url(r'^first_app/', include('apps.first_app.urls')),
    # This Blogs is targeting /apps/blogs/urls.py
    url(r'^/blogs$', include('apps.blogs.urls')),
    url(r'^blogs/', include('apps.blogs.urls')),


    # This is the admin path
    url(r'^admin/', admin.site.urls),
]
