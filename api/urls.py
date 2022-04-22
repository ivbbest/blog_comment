from django.urls import path, include
from rest_framework import routers
from api.views import PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', include(router.urls)),
    path('api/', include(router.urls))
]
