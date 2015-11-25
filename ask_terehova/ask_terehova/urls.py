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
#from ask_terehova_app.views import *
from ask_terehova_app import views


urlpatterns = [
    url(r'^$', views.main_page, name="main_page"),
    url(r'^pages/(?P<page_number>\d+)', views.index, name="index"),
    url(r'^base/', views.base, name="base"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ask/', views.ask, name="ask"),
    url(r'^hot/', views.hot, name="hot"),
    url(r'^tag/(?P<tag_text>\w+)', views.tag, name="tag"), 
    url(r'^login/', views.login, name="login"),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^question/(?P<question_id>\d+)', views.question, name="question"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


