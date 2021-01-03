from django.utils import timezone
from django.db import models
from DjangoForDnD import settings


class Person(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    map = models.CharField(max_length=50, default="")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name