from django.urls import path , re_path
from django.conf.urls import include, url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('dispositivo', views.DispositivoView, base_name = 'Dispositivo')

urlpatterns = [       
    re_path(r'^', include(router.urls)),
    re_path(r'^dispositivo/$', views.DispositivoList.as_view())
    # url(
    #     r'^dispositivo/(?P<pk>\d+)/$',
    #     views.DispositivoView.as_view({'get': 'get'}),
    #     name='Dispositivo-get',
    # ),
    # url(
    #     r'^dispositivo/change/(?P<pk>\d+)/$',
    #     views.DispositivoView.as_view({'put': 'change_url'}),
    #     name='Dispositivo-change_url',
    # ),
]