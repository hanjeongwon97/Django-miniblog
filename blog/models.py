from django.db import models

# Create your models here.
class Blog(models.Model):
    #objects = models.Manager() # h : views.py 에 Blogs object 오류 해결하기 위해 추가함
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
        