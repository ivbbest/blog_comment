from django.urls import path, include
from rest_framework import routers
from api.views import PostViewSet, CommentViewSet


router_post = routers.DefaultRouter()
router_post.register(r'post', PostViewSet, basename='post')
print(router_post.urls)

router_comment = routers.DefaultRouter()
router_comment.register(r'comment', CommentViewSet, basename='comment')
print(router_comment.urls)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/posts/', include(router_post.urls)),   # http://127.0.0.1:8000/api/v1/post/
    path('api/v1/comments/', include(router_comment.urls)),   # http://127.0.0.1:8000/api/v1/comments/
]
