from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    when = models.CharField(max_length=30,blank=True,null=True)
    # slug = models.SlugField()
    about = models.TextField()
    date = models.DateField(auto_now_add=True)
    # thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
