from django.conf.urls import patterns, include

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',

    (r'^test/',include('walk_python.article.articleUrls')),
    
    (r'^article/',include('walk_python.article.articleUrls')),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
