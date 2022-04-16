from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts',
                              on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.title, self.body)

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments',
                              on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments',
                             on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    def __str__(self):
        return "%s %s" % (self.body, self.parent)

    class Meta:
        ordering = ['created']

    class MPTTMeta:
        order_insertion_by = ['name']
