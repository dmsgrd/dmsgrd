from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings

urlpatterns = [
    # Examples:

    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'homepage.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^newsletter/', 'homepage.views.home', name='newsletter'),
    url(r'^cv/', 'homepage.views.cv', name='cv')
]

urlpatterns += staticfiles_urlpatterns()
