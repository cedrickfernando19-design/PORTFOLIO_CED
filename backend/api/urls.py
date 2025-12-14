from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, CertificateViewSet

router = routers.DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("certificates", CertificateViewSet)

urlpatterns = [
    path("", include(router.urls))
]
