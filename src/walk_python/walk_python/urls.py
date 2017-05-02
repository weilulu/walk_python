from django.conf.urls import patterns, include


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',

    (r'^test/',include('walk_python.article.articleUrls')),
    (r'^admin/',include('walk_python.admin.adminUrls')),
    (r'^article/',include('walk_python.article.articleUrls')),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
