from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=255)
    positive_count = models.IntegerField()
    negative_count = models.IntegerField()
    time_asked = models.DateTimeField(auto_now_add=True)
