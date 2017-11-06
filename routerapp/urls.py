"""routerapp URL Configuration"""

from django.conf.urls import url , include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name = 'login.html') , name = 'home'),
    url(r'^router/', include('router.urls')),
    url(r'^login$', auth_views.login , {'template_name': 'router/main.html'} , name = 'userLogin'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'} , name='userLogout'),
    
]
