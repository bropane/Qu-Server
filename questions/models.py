from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=255)
    positive_count = models.IntegerField(default=0)
    negative_count = models.IntegerField(default=0)
    time_asked = models.DateTimeField(auto_now_add=True)
