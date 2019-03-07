from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
  """
  タグ
  """
  name = models.CharField(null=False, max_length=64)
  def __str__(self):
    return self.name

class Post(models.Model):
  """
  記事のモデル
  """
  title     = models.CharField(null=False, max_length=128)
  text      = models.TextField(null=False, max_length=1024)
  date_post = models.DateTimeField(null=False, auto_now=True)
  date_update = models.DateTimeField(null=False)
  term_start  = models.DateTimeField(null=False)
  term_end    = models.DateTimeField(null=False)
  tags        = models.ManyToManyField(Tag, related_name='post_tag')
  user        = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    return self.title
