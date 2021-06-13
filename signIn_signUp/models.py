from django.db import models


class Details(models.Model):
    username=models.CharField(max_length=1000)
    email=models.EmailField(max_length=1000)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=10000)

    def __str__(self):
        return self.username