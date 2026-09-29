from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        title = mopdels.CharField(max_length=250)
        slug = models.SlugField(max_length=250)
        author = models.ForeignKey(User, on|_delete=models.CASCADE,related_name= 'blog_post')

        body = models. TextChoices()
        publish = models.DateTimeField(default=timezone.now)
        created = models.DateTimeField(auto_now_add=True)
        status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)

        class Meta:
            ordering=['-publish']
            indexes=[
                models.Index(fields=['-publish'])
            ]
        def _str_(self):
            return self.title