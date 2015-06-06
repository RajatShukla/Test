import django
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from pcap_uitl import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DevUtils.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.indexView),
    )


