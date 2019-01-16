from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    blogger = models.ForeignKey(User)
    title = models.CharField(max_length=20)
    text_area = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    like = models.BooleanField(default=False)






