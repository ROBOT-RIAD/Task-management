from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,SubtaskViewSet,TaskDetailView

router = DefaultRouter()
router.register('all', TaskViewSet,basename="all")
router.register('subtasks',SubtaskViewSet,basename="sub")

urlpatterns = [
    path('', include(router.urls)),
    path('all/<int:pk>/', TaskDetailView.as_view(), name='item-detail'),
]