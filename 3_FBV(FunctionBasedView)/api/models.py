from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=144)
    body = models.TextField()
    answer = models.IntegerField()