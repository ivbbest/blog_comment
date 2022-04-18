from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.title, self.body)

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    body = models.TextField(blank=False)
    author = models.CharField(max_length=100, blank=True)
    post = models.ForeignKey('Post', related_name='comments',
                             on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.body, self.post)

    class Meta:
        ordering = ('created',)

    class MPTTMeta:
        order_insertion_by = ['name']
