__author__ = 'RAJAT'
import django
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from telecom_utils import views
urlpatterns = patterns(

    url(r'',views.indexView),
    url(r'pcapUpload$',views.fileUpload),
    #url(r'/pcapDownload',views.fileDownloadForPcap),
    url(r'pcapDownload$',views.testFile),
    url(r'uploaded_files/(?P<fileName>\S+)/$',views.testDownload),
    url(r'smsPDU/$',views.smsHandler),
    url(r'pcapGeneration/$',views.pcapGenHandler),
    url(r'search_form/$', views.search_form),
    url(r'search/$', views.search)

    )