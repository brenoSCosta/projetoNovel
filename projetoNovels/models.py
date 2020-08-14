from django.db import models

# Create your models here.


class User(models.Model):
    nickname = models.CharField(max_length=16)
    login = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.nickname
