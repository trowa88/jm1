from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from building import views

router = DefaultRouter()
router.register(r'buildings', views.BuildingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
