from django.urls import path , re_path
from django.conf.urls import include, url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('gps', views.GpsList, base_name = 'Gps')

urlpatterns = [       
    re_path(r'^', include(router.urls)),
    re_path(r'^gps/$', views.GpsList.as_view())
    # url(
    #     r'^gps/(?P<pk>\d+)/$',
    #     views.GpsView.as_view({'get': 'get'}),
    #     name='Gps-get',
    # ),
    # url(
    #     r'^gps/change/(?P<pk>\d+)/$',
    #     views.GpsView.as_view({'put': 'change_url'}),
    #     name='Gps-change_url',
    # ),
]