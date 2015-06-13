import django
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from conversion import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DevUtils.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^/hex_conv',views.hex_conv),
    url(r'^/ip_conv',views.ip_conv),
    url(r'^/date_time_conv',views.date_time_conv),
    url(r'^$',views.indexView),
    )


