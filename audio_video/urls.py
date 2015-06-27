import django
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from audio_video import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DevUti
    # ls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^/audio_info$',views.audio_info),
    url(r'^/video_info$',views.video_info),
    url(r'^/youtube_video_info',views.youtube_video_info),
    url(r'^/test', views.test),
    url(r'^$',views.indexView),
    )


