from django.urls import path , re_path
from django.conf.urls import include, url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('unidades', views.UnidadesView, base_name = 'Unidades')

urlpatterns = [       
    re_path(r'^', include(router.urls)),
    re_path(r'^profile/$', views.UnidadesList.as_view())
    # url(
    #     r'^unidades/(?P<pk>\d+)/$',
    #     views.UnidadesView.as_view({'get': 'get'}),
    #     name='Unidades-get',
    # ),
    # url(
    #     r'^unidades/change/(?P<pk>\d+)/$',
    #     views.UnidadesView.as_view({'put': 'change_url'}),
    #     name='Unidades-change_url',
    # ),
]