"""the_story URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from building.views import BuildingViewSet
from comments.views import BuildingCommentViewSet, BuildingCommentLikeViewSet, BuildingPostCommentViewSet, \
    BuildingPostCommentLikeViewSet
from story_user import views
from the_story.settings import base

building_router = routers.DefaultRouter()
building_router.register(r'building', BuildingViewSet)
building_router.register(r'building-comment', BuildingCommentViewSet)
building_router.register(r'building-comment-like', BuildingCommentLikeViewSet)
building_router.register(r'building-post-comment', BuildingPostCommentViewSet)
building_router.register(r'building-post-comment-like', BuildingPostCommentLikeViewSet)

schema_view = get_swagger_view(title='The Story API', url='/api/')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(building_router.urls, namespace='api')),
    url(r'^o/', include('oauth2_provider.urls', namespace="oauth2_provider")),
    url(r'^sign_up/', views.SignUp.as_view(), name='sign_up1'),
    url(r'^docs/', schema_view),
]

urlpatterns += static('/upload_files/', document_root=base.MEDIA_ROOT)
urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)

