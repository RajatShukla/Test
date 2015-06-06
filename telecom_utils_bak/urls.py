__author__ = 'RAJAT'
import django
from django.conf.urls import patterns, include, url
from telecom_utils import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DevUtils.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.indexView),
    #url(r'^/pcapUpload',views.fileUpload)
    )
