from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'projects', ListViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
