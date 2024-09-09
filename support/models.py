from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def _str__(self):
        return f'Message from {self.email}'
    

class Waitlist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Waitlist request - {self.email}'