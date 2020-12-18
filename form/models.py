from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=230)
    phone = models.CharField(max_length=12)
    msg = models.TextField()

    def __str__(self):
        return self.name
    