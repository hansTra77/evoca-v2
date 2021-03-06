"""evoca_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from rest_framework.authtoken import views

from django.conf import settings
from django.conf.urls.static import static

from core.views import *
from web_client.views import *


# ------ API First level routing ------

router = DefaultRouter()
router.register(r'channel', ChannelAPIView)
router.register(r'records', RecordAPIView)

# ------ API Second level routing ------

channel_router = routers.NestedSimpleRouter(router, r'channel', lookup='channel')
channel_router.register(r'records', RecordAPIView, base_name='records')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api-token-auth/', views.obtain_auth_token),
	url(r'^api/v1/', include(router.urls)),
	url(r'^api/v1/', include(channel_router.urls)),

    # ----------- Web-Client URLS ---------

    url(r'^$', ChannelsListView.as_view(), name='channel-view'),
    url(r'^(?P<channel>[-_\w]+)/$', RecordsListView.as_view(), name='records-list-view')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
