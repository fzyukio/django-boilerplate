from django.db import models


class Document(models.Model):
    content = models.TextField(max_length=255)
    type = models.CharField(max_length=31)

    views = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.content, self.type)
