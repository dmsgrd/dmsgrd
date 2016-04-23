from django.conf.urls import include, url
from django.contrib import admin
from . import settings

urlpatterns = [
    # Examples:

    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'homepage.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^newsletter/', 'homepage.views.home', name='home')

]
