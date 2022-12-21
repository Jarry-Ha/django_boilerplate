from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    cpu = models.IntegerField()
    ram = models.IntegerField()
    disk = models.IntegerField()

    class Meta:
        ordering = ['created']