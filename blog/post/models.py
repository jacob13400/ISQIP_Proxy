from django.db import models
from django.conf import settings

# Create your models here
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

class Category(TimeStampedModel):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

