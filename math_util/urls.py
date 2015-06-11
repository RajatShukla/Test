import django
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from math_util import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DevUti
    # ls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^/number_theoretic',views.number_theoretic),
    url(r'^/pow_log',views.pow_log),
    url(r'^/trigon_fun',views.trigon_fun),
    url(r'^/hyperbolic_fun',views.hyperbolic_fun),
    url(r'^/matrix_fun',views.matrix_fun),
    url(r'^$',views.indexView),
    )



