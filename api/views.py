from api.models import Post, Comment
from rest_framework import generics, permissions, viewsets
from api.serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_fields = ["post"]

    def get_queryset(self):
        if self.action == "list":
            return Comment.objects.root_nodes().select_related(
                "parent", "post"
            )
        return Comment.objects.all().select_related("parent", "post")