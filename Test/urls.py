import django
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from encoder_decoder import urls as encoderDecoderURL
from audio_video import urls as audioVideoURL
from conversion import urls as conversionURL
from date_time import urls as dateTimeURL
from hex_editor import urls as hexEditorURL
from math_util import urls as mathURL
from pcap_uitl import urls as pcapURL
from telecom_utils import urls as telecomURL
from encryption_utils import urls as encryptionURL

from django.contrib import admin
from DevUtils1 import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DevUtils.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^about', views.aboutView),
    url(r'^contact', views.contactView),
    url(r'^blog', views.blogView),
    url(r'^services', views.servicesView),
    url(r'^product', views.productView),
    url(r'^encoderDecoder', include(encoderDecoderURL)),
    url(r'^audio_video', include(audioVideoURL)),
    url(r'^conversion', include(conversionURL)),
    url(r'^date_time', include(dateTimeURL)),
    url(r'^hex_editor', include(hexEditorURL)),
    url(r'^math_util', include(mathURL)),
    url(r'^pcap_util', include(pcapURL)),
    url(r'^telecom_util',include(telecomURL)),
    url(r'^encrypt_util', include(encryptionURL)),
    url(r'^$', views.indexView),



)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
