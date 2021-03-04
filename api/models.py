from django.db import models

class Userss(models.Model):
    name = models.CharField(max_length=200,null = True)
    username = models.CharField(max_length=200, null = True)
    email = models.EmailField(null = True)
    phone = models.CharField(max_length=200, null = True, blank=True)
    website = models.CharField(max_length=200, null = True, blank=True)

    def __str__(self):
        return self.name