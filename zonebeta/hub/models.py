from django.db import models


class Hubmodel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=400)

    def __str__(self):
        return self.title