from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Article(models.Model):
    """
    帖子表
    """
    title = models.CharField(max_length=255,unique=True)
    category = models.ForeignKey('Category')
    priority = models.IntegerField(default=1000)
    author = models.ForeignKey('UserProfile')
    content = models.TextField(max_length=10000)
    breif = models.TextField(max_length=512,default='None...')
    head_img = models.ImageField(upload_to='photos/icon')
    publish_date = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    """
    评论表
    """
    article = models.ForeignKey('Article')
    parent_id = models.ForeignKey('Comment',related_name='parent_comment',blank=True,null=True)
    comment = models.TextField(max_length=1024)
    user = models.ForeignKey('UserProfile')
    date = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.comment

class Thumb(models.Model):
    """
    点赞表
    """
    article = models.ForeignKey('Article')
    action_choices = (('thumb_up','Thumb Up'),('view_count', 'View Count'))
    action = models.CharField(choices=action_choices,max_length=32)
    user = models.ForeignKey('UserProfile')
    def __unicode__(self):
        return "%s : %s" % (self.article.title, self.action)
class Category(models.Model):
    """
    版块分类
    """
    name = models.CharField(max_length=32,unique=True)
    enabled = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    """
    用户表
    """
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64)
    user_groups = models.ManyToManyField('Usergroup')
    friends = models.ManyToManyField('self',blank=True)
    online = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name



class Usergroup(models.Model):
    """
    用户组表
    """
    name = models.CharField(max_length=32,unique=True)
    def __unicode__(self):
        return self.name