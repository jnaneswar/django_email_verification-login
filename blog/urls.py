from django.conf.urls import url, include
from django.contrib.auth import views as auth_views,login,logout

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
     #url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^out$', views.logout_view, name='out'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]