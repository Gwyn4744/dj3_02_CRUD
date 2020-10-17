from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
