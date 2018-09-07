from django.conf.urls import re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    re_path(r'^auth/?', include('rest_framework.urls')),
    re_path(r'^users/?$', views.UserView.as_view()),
    re_path(r'users/(?P<pk>[0-9]+)/?$', views.UserDetailsView.as_view()),
    re_path(r'^get-token/?', obtain_auth_token),
    re_path(r'^faces/?$', views.FaceCreate.as_view()),
    re_path(r'^$', views.index),
]