"""AskSoldatov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from ask_terehova_app.views import *


urlpatterns = [
    url(r'^$', main_page),
    url(r'^pages/(?P<page_number>\d+)', index),
    url(r'^base/', base),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ask/', ask),
    url(r'^index/', index),
    url(r'^hot/', hot),
    url(r'^tag/(?P<tag_text>\w+)', tag),
    url(r'^tag/', tag),
    url(r'^login/', login),
    url(r'^signup/', signup),
    url(r'^question/(?P<question_id>\d+)', question),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


