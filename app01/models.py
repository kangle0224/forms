from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.username
