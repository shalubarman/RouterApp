from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from rest_framework.authtoken import views as rest_framework_views

from .views import RouterList, RouterDetail

app_name = 'router'

urlpatterns = [
    url(r'^api$', RouterList.as_view() , name = 'routerlist'),
    url(r'^api/(?P<loopback>[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})$', RouterDetail.as_view() , name = 'routerdetail'),
  	url(r'^$', login_required(TemplateView.as_view(template_name = 'router/main.html')) , name = 'home'),
    url(r'^search/ip$', login_required(TemplateView.as_view(template_name = 'router/searchip.html')) , name = 'searchbyip'), 
    url(r'^search/id$', login_required(TemplateView.as_view(template_name = 'router/searchid.html')) , name = 'searchbyid'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)