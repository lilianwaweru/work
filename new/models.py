from django.db import models

# Create your models here.
class Work(models.Model):
    receipient = models.EmailField()
    sender = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)

    def save_Work(self):
        self.save()
