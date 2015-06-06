__author__ = 'RAJAT'
import django
from django.conf.urls import patterns, include, url
from encryption_utils import views
#URL for encryption decryption utility
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DevUtils.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^/hash$',views.hashing),
    url(r'^/encr_decr',views.encrypt_decrypt),
    url(r'^/rsa',views.rsa_algo),
    url(r'^/',views.index_view)


    )