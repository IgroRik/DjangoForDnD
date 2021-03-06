from django.utils import timezone
from django.db import models
from DjangoForDnD import settings


class Person(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    icon = models.ImageField(null=False, default="images/placeholder.png", blank=True, upload_to="images", verbose_name='Изображение')
    role = models.CharField(max_length=50, default="")
    map = models.CharField(max_length=50, default="")
    created_date = models.DateTimeField(default=timezone.now)
    alive = models.BooleanField(default="True")

    def __str__(self):
        return self.name
