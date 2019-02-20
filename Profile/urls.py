from django.urls import path , re_path
from django.conf.urls import include, url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('profile', views.ProfileView, base_name = 'Profile')

urlpatterns = [       
    re_path(r'^', include(router.urls)),
    re_path(r'^profile/$', views.ProfileList.as_view())
    # url(
    #     r'^profile/(?P<pk>\d+)/$',
    #     views.ProfileView.as_view({'get': 'get'}),
    #     name='Profile-get',
    # ),
    # url(
    #     r'^profile/change/(?P<pk>\d+)/$',
    #     views.ProfileView.as_view({'put': 'change_url'}),
    #     name='Profile-change_url',
    # ),
]