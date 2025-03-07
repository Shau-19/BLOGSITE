"""
URL configuration for First project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blogsite import views





urlpatterns = [
    #path('',views.home, name='home'),
    path('',views.home, name='home'),
    path("story/",views.story,name="story"),
    path("admin-panel/", admin.site.urls),
    path("aboutUs/",views.aboutUS,name='About'),
    path("article/",views.article, name='article'),
    path("storymenu/",views.storymenu, name='storymenu'),
    path("share/",views.share, name='share'),
    path("uploadB/",views.upload_blog, name='uploadB'),
    path("uploadS/",views.upload_story, name='uploadS'),
    path("uploadA/",views.upload_article, name='uploadA'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
