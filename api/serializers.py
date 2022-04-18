from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(
        read_only=True, method_name="get_child_comments"
    )
    class Meta:
        model = Comment
        fields = "__all__"

    def get_child_comments(self, obj):
        serializer = CommentSerializer(instance=obj.get_children(), many=True)
        return serializer.data
